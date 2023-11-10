#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node.
# Each country node should have a name attribute.
# The third node name should be Panama.
#

import xml.etree.ElementTree as ET

root = ET.Element("root")
country = ["a", "b", "Panama"]

for x in country:
  ET.SubElement(root, "country").set("name", x)

tree = ET.ElementTree(root)
  
with open("/tmp/vulnerable-countries.xml", "wb") as file:
    tree.write(file)
