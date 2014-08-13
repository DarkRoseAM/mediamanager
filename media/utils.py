# =============================================================================
# CLASSES
# =============================================================================

# Standard Imports
from datetime import datetime
import re

# Third Party Imports
from xml.etree import ElementTree

# Application Imports
from .models import Media

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================

def getMedia(inputString):
    elementTree = ElementTree.fromstring(
        re.sub(' xmlns="[^"]+"', '', inputString, count=1),
    )

    results = []

    for fileElement in elementTree.getchildren():
        if fileElement.tag == 'file':
            values = {}

            for element in fileElement.getchildren():
                values[element.tag] = element.text

            values.pop('filename')

            releasedate = values.get('releasedate')
            if releasedate:
                dt = datetime.strptime(releasedate, '%m/%d/%Y')
                values['releasedate'] = dt.strftime('%Y-%m-%d')

            results.append(Media(**values))

    return results