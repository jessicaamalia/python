import os
import win32api
import win32print
import shutil
from glob import glob
from PyPDF2 import PdfMerger

# Create a temp folder
current_directory = os.getcwd()
temp_directory = os.path.join(current_directory, r'temp_folder')
if not os.path.exists(temp_directory):
   os.makedirs(temp_directory)

# A List containing the system printers
all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
# Ask the user to select a printer
#printer_num = int(input("Choose a printer:\n"+"\n".join([f"{n} {p}" for n, p in enumerate(all_printers)])+"\n"))
# set the default printer
win32print.SetDefaultPrinter("Microsoft Print to PDF")

Prefix = ['DOR', 'PGU']
filePath  = os.getcwd()+ '\\'
fileList  = []

for CodePrefix in Prefix:
   for path, currentDirectory, files in os.walk(filePath):
      for fileName in files:
         if fileName.startswith(CodePrefix):
            fileList.append(fileName)

# Print Microsoft to PDF
for CodePrefix in Prefix:
   for fileName in fileList:
      if CodePrefix not in fileName:
         continue
      elif fileName.startswith("DOR"):
         win32api.ShellExecute(0, "print", filePath + fileName, None,  ".",  0)