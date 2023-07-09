import os
import shutil

# Setting the source and the destination folders
src  = os.getcwd()+ '\\'

# Input filename
print('Enter file name to be deleted (ex., A.py):')
file = input()
src_file = src + file

if os.path.exists(src_file)==True:
    subdirs = [x[0] for x in os.walk(src)]                                                                            
    for dst in subdirs:                                                                                            
        # file names
        dst_file = dst + "\\" + file
        if src!=dst and os.path.exists(dst_file)==True:
            os.remove(dst_file)
            print(dst_file + ' was removed')
else:
    print('File not found')

input('Press ENTER to exit')
  