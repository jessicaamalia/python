import os
import shutil

# Setting the source and the destination folders
src  = os.getcwd()+ '\\'

# Input filename
print('Enter file name to be copied (ex., A.py):')
file = input()
src_file = src + file

if os.path.exists(src_file)==True:
    subdirs = [x[0] for x in os.walk(src)]                                                                            
    for dst in subdirs:                                                                                            
        dst_file = dst + "\\" + file
        if src!=dst and os.path.exists(dst_file)==False:
            shutil.copyfile(src_file,dst_file)
            print('File was copied to ' + dst_file)
else:
    print('File not found')

input('Press ENTER to exit')
  