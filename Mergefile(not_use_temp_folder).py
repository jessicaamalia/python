import os
from PyPDF2 import PdfMerger

Prefix = ['DOR', 'PGU']
filePath  = os.getcwd()+ '\\'
fileList  = []

for CodePrefix in Prefix:
   for path, currentDirectory, files in os.walk(filePath):
      for fileName in files:
         if fileName.startswith(CodePrefix):
            fileList.append(fileName)

for fileName in fileList:
    if fileName.startswith("PGU"):
        pbr=(filePath + fileName).rpartition('_')[-1]
        pbr=pbr.rpartition('.')[0]

# Append & Merge all PDFs starting with similar names 
for CodePrefix in Prefix:
    merger = PdfMerger()
    for fileName in fileList:
        if CodePrefix not in fileName:
            continue
        merger.append(filePath + fileName)
    
    merger.write(filePath + CodePrefix + '.pdf')
    merger.close()

# Combine PGU and DOR
pdfs = ['PGU.pdf', 'DOR.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

folder_name = os.path.basename(os.getcwd())
merger.write(pbr + '_Merged_' + folder_name + '.pdf')
merger.close()

# Delete file DOR and PGU
os.remove('PGU.pdf')
os.remove('DOR.pdf')