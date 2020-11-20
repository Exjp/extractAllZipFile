import glob
from zipfile import ZipFile
import os
from os.path import basename


txtfiles = []
txtfilesname = []
for file in glob.glob("*.zip"):
    txtfiles.append(file)
    tmp =  basename(file)
    fileName, fileExtension = os.path.splitext(file)
    txtfilesname.append(fileName)


for file, folder in zip(txtfiles,txtfilesname):

    os.mkdir(folder)

    with ZipFile(file,'r') as zip:
        print('extraction '+file+'...')
        zip.extractall(folder)

    os.remove(file)

