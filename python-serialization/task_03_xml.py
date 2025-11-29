#!/usr/bin/env python3
"""Module for serializing and deserializing Python dictionaries using XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file
    Args:
        dictionary (dict): Dictionary to serialize
        filename (str): Output XML filename
    """
    # Create the root element
    root = ET.Element("data")

    # Add each dictionary element as a child tag
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create an ElementTree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes an XML file back into a Python dictionary
    Args:
        filename (str): XML filename to read
    Returns:
        dict: Deserialized dictionary
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    # Rebuild dictionary from XML tree
    for element in root:
        result_dict[element.tag] = element.text

    return result_dict
