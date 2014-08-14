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

def _convertDate(values):
    """ Convert DateFields to Django's desired formatting.
    """
    # List of DateFields that need to be converted.
    dateFields = ['releasedate']

    for field in dateFields:
        # See if the field is in the dictionary.
        value = values.get(field)

        if value:
            # Create a DateTime from the given value.
            dt = datetime.strptime(value, '%m/%d/%Y')
            # Update the dictionary with the reformated DateTime.
            values[field] = dt.strftime('%Y-%m-%d')

# =============================================================================

def _getFilesFromXML(inputString):
    """ Get a list of files from an XML manifest.
    """
    # Convert the inputString to ElementTree format.
    elementTree = ElementTree.fromstring(
        re.sub(' xmlns="[^"]+"', '', inputString, count=1),
    )

    results = []

    # Loop over each of the children in the ElementTree.
    for fileElement in elementTree.getchildren():
        # Ensure that they are files.
        if fileElement.tag == 'file':
            values = {}

            # Loop over each of the keys in the file.
            for element in fileElement.getchildren():
                # Add the key and its text value to the values dictionary.
                values[element.tag] = element.text

            # Convert DateFields to Django's desired formatting.
            _convertDate(values)
            # Add the values dictionary to the list of files.
            results.append(values)

    return results

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================

def processUpload(inputFile):
    """ Create the necessary database entries from the given manifest file.
    """
    inputString = inputFile.read()

    # Create Manifest model.
    manifest = models.Manifest(
        file=inputFile,
    )
    manifest.save()

    # Create Upload model.
    upload = models.Upload(
        manifest=manifest,
    )
    upload.save()

    # Loop over the list of files from an XML manifest.
    for values in _getFilesFromXML(inputString):
        # Create MediaData model.
        mediaData = models.MediaData(
            barcode=values.get('barcode'),
            contenttype=values.get('contenttype'),
            language=values.get('barcode'),
            manifest=manifest,
            releasedate=values.get('releasedate'),
            title=values.get('title'),
            version=values.get('version'),
        )
        mediaData.save()



def something():
        # Create Media model.
        media = models.Media(
            data=mediaData,
            file=values.get('filename'),
        )
        media.save()
