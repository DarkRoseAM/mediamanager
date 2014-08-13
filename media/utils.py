# =============================================================================
# CLASSES
# =============================================================================

# Standard Imports
from datetime import datetime
import re

# Third Party Imports
from xml.etree import ElementTree

# Application Imports
from .models import MediaData

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================

def getManifests(manifestfile):
    elementTree = ElementTree.fromstring(
        re.sub(' xmlns="[^"]+"', '', manifestfile.read(), count=1),
    )

    results = []

    for fileElement in elementTree.getchildren():
        if fileElement.tag == 'file':
            values = {
                'manifestfile': manifestfile,
            }

            for element in fileElement.getchildren():
                values[element.tag] = element.text

            values.pop('filename')

            releasedate = values.get('releasedate')
            if releasedate:
                dt = datetime.strptime(releasedate, '%m/%d/%Y')
                values['releasedate'] = dt.strftime('%Y-%m-%d')

            results.append(MediaData(**values))

    return results
