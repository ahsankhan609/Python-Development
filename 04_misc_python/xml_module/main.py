"""NOTE: XML is a markup language that is used to store and transport data.

KEY POINTS:
* It is a text-based format that is designed to be both human-readable and machine-readable.
* It is a part of python standard library.
* It is a lightweight markup language used to store and transport data.
* It is a hierarchical data format.
* It is a self-describing language.
* It is a platform-independent language.
* It is a language-independent language.
* every file must have a root tag, that should envelope all the other tags.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

# Parse XML into Element Tree and extract the data

# Resolve relative to this script's directory so the file is found regardless of CWD.
tree: ET.ElementTree[ET.Element] = ET.parse(Path(__file__).parent / 'data.xml')
root: ET.Element = tree.getroot()

# Root
# print(root.tag)  # returns the root tag name
# print(len(root))  # returns the number of children of the root tag
# print(root.attrib)  # returns the attributes of the root tag
# print(root.text)  # returns the text content of the root tag

# Access Root Child
# print(root[0].tag)  # returns the tag name of the first child of the root tag
# # returns the number of children of the first child of the root tag
# print(len(root[0]))
# returns the attributes of the first child of the root tag

# Loop over Root Children
for child in root:
    print(child.tag)  # returns the tag name of the child
    # The direct text of <stock> element is likely just a newline and spaces, since actual data is in subelements
    # print meaningful whitespace-stripped text
    print(child.text.strip() if child.text else "")
    # child.attrib is empty because <stock> has no attributes in data.xml; show a message for clarity
    if child.attrib:
        print(child.attrib)
    else:
        print("{} (no attributes)")

    # Optionally, print subelement tags and values
    for subchild in child:
        print(f"  {subchild.tag}: {subchild.text.strip() if subchild.text else ''}")
    print("---")

# Root Grandchildren
# print(root[0][o].tag)
# print(root[0][o].text)
# print(root[0][1].tag)
# print(root[0][1].text)
# print(root[1][2].tag) # price
# print(root[1][2].text)
