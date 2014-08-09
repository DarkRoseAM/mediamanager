import re
from xml.etree import ElementTree

def _remove_xmlns(input_file):
    """Removes the xmlns attribute from XML files, then returns the element
    """
    # We're going to open the file as a string and remove the xmlns, as
    # it doesn't do a lot for us when working with CDLs, and in fact
    # just clutters everything the hell up.
    with open(input_file, 'r') as xml_file:
        xml_string = xml_file.read()

    xml_string = re.sub(' xmlns="[^"]+"', '', xml_string, count=1)
    return ElementTree.fromstring(xml_string)

def parseXML(input_file):
    """Parses a .cc file for ASC CDL information
    **Args:**
    input_file : (str|<ElementTree.Element>)
    The filepath to the CC or the ``ElementTree.Element`` object.
    **Returns:**
    (:class:`ColorCorrection`)
    The :class:`ColorCorrection` described within.
    **Raises:**
    ValueError:
    Bad XML formatting can raise ValueError is missing required
    elements.
    A CC file is really only a single element of a larger CDL or CCC XML file,
    but this element has become a popular way of passing around single shot
    CDLs, rather than the much bulkier CDL file.
    A sample CC XML file has text like:
    ::
    <ColorCorrection id="cc03340">
    <SOPNode>
    <Description>change +1 red, contrast boost</Description>
    <Slope>1.2 1.3 1.4</Slope>
    <Offset>0.3 0.0 0.0</Offset>
    <Power>1.0 1.0 1.0</Power>
    </SOPNode>
    <SatNode>
    <Saturation>1.2</Saturation>
    </SatNode>
    </ColorCorrection>
    Additional elements can include multiple descriptions at every level,
    a description of the input colorspace, and a description of the viewing
    colorspace and equipment.
    """
    if type(input_file) is str:
        root = _remove_xmlns(input_file)
        file_in = input_file
    else:
        root = input_file
        file_in = None

    if not root.tag == 'ColorCorrection':
        # This is not a CC file...
        raise ValueError('CC parsed but no ColorCorrection found')

    try:
        cc_id = root.attrib['id']
    except KeyError:
        raise ValueError('No id found on ColorCorrection')

    cdl = correction.ColorCorrection(cc_id)
    if file_in:
        cdl.file_in = file_in

    # Grab our descriptions and add them to the cdl.
    cdl.parse_xml_descs(root)
    # See if we have a viewing description.
    cdl.parse_xml_viewing_desc(root)
    # See if we have an input description.
    cdl.parse_xml_input_desc(root)

    def find_required(elem, names):
        """Finds the required element and returns the found value.
        Args:
        root : <ElementTree.Element>
        The element to search in.
        names : [str]
        A list of names the element might be under.
        Raises:
        ValueError:
        If element does not contain the required name.
        Returns:
        <ElementTree.Element>
        """
        found_element = None
        for possibility in names:
            found_element = elem.find(possibility)
            if found_element is not None:
                break
        # element might never have been triggered.
        if found_element is None:
            raise ValueError(
                'The ColorCorrection element could not be parsed because the '
                'XML is missing required elements: {elems}'.format(
                    elems=str(names)
                )
            )
        else:
            return found_element

    try:
        sop_xml = find_required(root, correction.SopNode.element_names)
    except ValueError:
        sop_xml = None

    try:
        sat_xml = find_required(root, correction.SatNode.element_names)
    except ValueError:
        sat_xml = None

    if sop_xml is None and sat_xml is None:
        raise ValueError(
            'The ColorCorrection element requires either a Sop node or a '
            'Sat node, and it is missing both.'
        )

    if sop_xml is not None:
        cdl.slope = find_required(sop_xml, ['Slope']).text.split()
        cdl.offset = find_required(sop_xml, ['Offset']).text.split()
        cdl.power = find_required(sop_xml, ['Power']).text.split()
        # Calling the slope, offset and power attributes on the cdl will
        # have created an instance of SopNode on cdl.sop_node, so we can
        # populate those descriptions.
        cdl.sop_node.parse_xml_descs(sop_xml)

    if sat_xml is not None:
        cdl.sat = find_required(sat_xml, ['Saturation']).text
        # In the same manor of sop, we can call the sat node now to set the
        # desc descriptions.
        cdl.sat_node.parse_xml_descs(sat_xml)
    return cdl
