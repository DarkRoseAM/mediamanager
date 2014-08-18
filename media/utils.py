# =============================================================================
# CLASSES
# =============================================================================

# Standard Imports
from datetime import datetime
import re

# Third Party Imports
from xml.etree import ElementTree

# Application Imports
from . import models

# =============================================================================
# PRIVATE FUNCTIONS
# =============================================================================


def _convert_date(values):
    """ Convert DateFields to Django's desired formatting.
    """
    # List of DateFields that need to be converted.
    date_fields = ['releasedate']

    for field in date_fields:
        # See if the field is in the dictionary.
        value = values.get(field)

        if value:
            # Create a DateTime from the given value.
            dt = datetime.strptime(value, '%m/%d/%Y')
            # Update the dictionary with the reformated DateTime.
            values[field] = dt.strftime('%Y-%m-%d')


def _create_model_instance(cls, *args, **kwargs):
        # Create an instance of the model.
        instance = cls(*args, **kwargs)

        try:
            # Is there an existing instance of the model?
            instance = cls.objects.get(pk=instance.get_id())
        except cls.DoesNotExist:
            # Use the instance we just created.
            instance.save()

        return instance


def _get_files_from_xml(input_string):
    """ Get a list of files from an XML manifest.
    """
    # Convert the inputString to ElementTree format.
    element_tree = ElementTree.fromstring(
        re.sub(' xmlns="[^"]+"', '', input_string, count=1),
    )

    results = []

    # Loop over each of the children in the ElementTree.
    for file_element in list(element_tree):
        # Ensure that they are files.
        if file_element.tag == 'file':
            values = {}

            # Loop over each of the keys in the file.
            for element in list(file_element):
                # Add the key and its text value to the values dictionary.
                values[element.tag] = element.text

            # Convert DateFields to Django's desired formatting.
            _convert_date(values)
            # Add the values dictionary to the list of files.
            results.append(values)

    return results


def _get_model_instances(cls, *args, **kwargs):
    try:
        # Is there an existing instance of the model?
        return cls.objects.filter(*args, **kwargs)
    except cls.DoesNotExist:
        return None


# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================


def process_upload(input_files):
    """ Create the necessary database entries from the given manifest file.
    """
    # Create Upload.
    upload = models.Upload()
    upload.save()

    for input_file in input_files:
        if input_file.name.split('.')[-1].lower() == 'xml':
            input_string = input_file.read()

            # Create ManifestFile.
            manifest = _create_model_instance(
                models.ManifestFile,
                file=input_file,
            )
            upload.manifests.add(manifest)

            # Loop over the list of files from an XML manifest.
            for values in _get_files_from_xml(input_string):
                # Create Record.
                record = _create_model_instance(
                    models.Record,
                    barcode=values.get('barcode'),
                    contenttype=values.get('contenttype'),
                    filename=values.get('filename'),
                    language=values.get('language'),
                    md5=values.get('md5'),
                    releasedate=values.get('releasedate'),
                    title=values.get('title'),
                    version=values.get('version'),
                )
                manifest.records.add(record)

                media = _get_model_instances(
                    models.MediaFile,
                    id=values.get('md5'),
                )
                if media:
                    record.media = media[0]
                    record.save()

        else:
            # Create MediaFile.
            media = _create_model_instance(
                models.MediaFile,
                file=input_file,
            )
            upload.media.add(media)

            records = _get_model_instances(
                models.Record,
                md5=media.get_id(),
            )

            if records:
                for record in records:
                    record.media = media
                    record.save()

    return upload
