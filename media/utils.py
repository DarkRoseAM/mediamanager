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

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================


def process_upload(input_file):
    """ Create the necessary database entries from the given manifest file.
    """
    input_string = input_file.read()

    # Create Manifest model.
    manifest = models.File(
        file=input_file,
    )
    manifest.save()

    # Create Upload model.
    upload = models.Upload(
        manifest=manifest,
    )
    upload.save()

    # Loop over the list of files from an XML manifest.
    for values in _get_files_from_xml(input_string):
        # Create Record model.
        record = models.Record(
            barcode=values.get('barcode'),
            contenttype=values.get('contenttype'),
            language=values.get('language'),
            manifest=manifest,
            releasedate=values.get('releasedate'),
            title=values.get('title'),
            version=values.get('version'),
        )
        record.save()
