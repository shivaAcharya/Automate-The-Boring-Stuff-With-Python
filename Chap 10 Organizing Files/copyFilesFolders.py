#Program to copy files/folders

import shutil, os
from pathlib import Path

p = Path(r'C:\Users\cvach\Desktop')
q = Path(r'E:\Google Drive')

shutil.copytree(p / 'Genuine Pasal', q / 'Genuine Pasal Backup')






