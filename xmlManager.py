import xml.etree.ElementTree as ET
from io import BytesIO

import os

#champ xml pour banni ou non, à exclure des fonctions getAliases, getnumberfromalias et random

def init():
    emptyXml()
    global tree
    tree = ET.parse('page.xml')
    global root
    root = tree.getroot()


def emptyXml():
   
    rootEmpty = ET.Element("users")
    treeEmpty = ET.ElementTree(rootEmpty)
    treeEmpty.write("page.xml",
           xml_declaration=True,encoding='utf-8',
           method="xml")


# vérifier que les champs sont uniques, vérifier que les champs sont corrects
def addUser(aliasValue, numberValue, keyValue):
    user = ET.Element('user')
    user.set("alias", aliasValue)
    number = ET.SubElement(user, "number")
    number.text = numberValue
    key = ET.SubElement(user, "key")
    key.text = keyValue
    root.append(user)


# Element.get pour trouver les attributs
def removeUser(name):
    for elem in root:
        if elem.attrib['alias'] == name:
            root.remove(elem)


def getNumberFromAlias(name):
    for elem in root:
        if elem.attrib['alias'] == name:
            for var in elem:
                if var.tag == "number":
                    return var.text
            break


#return une liste des alias dans la bdd
def getAliases():
    return [elem.attrib['alias'] for elem in root]


#on peut avoir le destinataire final
def randomUsers():
    print("TODO")


def main():
    addUser("Thierry", "+33666666666", "key")
    addUser("Jak", "+33626486623", "key2")
    x = getAliases()
    tree.write('page.xml', encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    init()
    main()

