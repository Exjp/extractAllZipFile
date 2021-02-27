from xml import etree
import xml.etree.ElementTree as ET
from io import BytesIO

import os

def emptyXml():
   
    root = ET.Element("users")
    doc = ET.SubElement(root, "user")
    
    ET.SubElement(doc, "number").text = "some value1"
    ET.SubElement(doc, "key").text = "some vlaue2"
    tree = ET.ElementTree(root)
    tree.write("page.xml",
           xml_declaration=True,encoding='utf-8',
           method="xml")

def main():
    emptyXml()

if __name__ == "__main__":
    main()