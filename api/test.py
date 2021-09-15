from zipfile import ZipFile
import os
from collections import Counter

file_name1 = "/home/nibmg/Desktop/folderpro/backend/api/zipfiles/2240111_TruseqNano_HYGWFDSXY_L1_R2_fastqc.zip"
file_name2 = "/home/nibmg/Desktop/folderpro/backend/api/zipfiles/2240111_TruseqNano_HYGWFDSXY_L1_R1_fastqc.zip"


counts = Counter()
for c_dir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        before_ext, extension = os.path.splitext(filename)
        counts[extension] += 1
with ZipFile(file_name2, 'r') as zip:
    zip.printdir()
    print(zip.infolist())

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall('zipfiles')
    print('Done!')
    print(dir(zip))
for extension, count in counts.items():
    ext = f"{extension:6}{count}"
    print("The Extension Name", type(ext))
# Path where we have to count files and directories
HOME_FOLDER = '/home/nibmg/Desktop/folderpro/backend/api/zipfiles/'

noOfFiles = 0
noOfDir = 0

for base, dirs, files in os.walk(HOME_FOLDER):
    print('Looking in : ', base)
    for directories in dirs:
        noOfDir += 1
    for Files in files:
        noOfFiles += 1
    print(dirs)

print(type(files))
print('Number of files', noOfFiles)
print('Number of Directories', noOfDir)
print('Total:', (noOfDir + noOfFiles))
