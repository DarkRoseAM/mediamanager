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
# GLOBALS
# =============================================================================

MANIFEST_TYPES = ['xml']

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


def _get_files_from_xml(input_string):
    """ Get a list of files from an XML manifest.
    """
    # Convert the inputString to ElementTree format.
    element_tree = ElementTree.fromstring(
        re.sub(' xmlns="[^"]+"', '', input_string, count=1),
    )

    results = []

    # Loop over each of the children in the ElementTree.
    for file_element in element_tree.getchildren():
        # Ensure that they are files.
        if file_element.tag == 'file':
            values = {}

            # Loop over each of the keys in the file.
            for element in file_element.getchildren():
                # Add the key and its text value to the values dictionary.
                values[element.tag] = element.text

            # Convert DateFields to Django's desired formatting.
            _convert_date(values)
            # Add the values dictionary to the list of files.
            results.append(values)

    return results


def _get_model_instance(cls, *args, **kwargs):
        # Create an instance of the model.
        instance = cls(*args, **kwargs)

        try:
            # Is there an existing instance of the model?
            instance = cls.objects.get(pk=instance.get_id())
        except cls.DoesNotExist:
            # Use the instance we just created.
            instance.save()

        return instance

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================


def process_upload(input_files):
    """ Create the necessary database entries from the given manifest file.
    """
    # Create Upload model.
    upload = models.Upload()
    upload.save()

    for input_file in input_files:
        input_string = input_file.read()

        # Create Media model.
        media = _get_model_instance(
            models.Media,
            file=input_file,
            upload=upload,
        )

        if input_file.name.split('.')[-1].lower() in MANIFEST_TYPES:
            # Loop over the list of files from an XML manifest.
            for values in _get_files_from_xml(input_string):
                # Create Record model.
                _get_model_instance(
                    models.Record,
                    barcode=values.get('barcode'),
                    contenttype=values.get('contenttype'),
                    manifest=media,
                    filename=values.get('filename'),
                    language=values.get('language'),
                    md5=values.get('md5'),
                    releasedate=values.get('releasedate'),
                    title=values.get('title'),
                    upload=upload,
                    version=values.get('version'),
                )
