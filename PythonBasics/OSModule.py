import os

curDir = os.getcwd()
print(curDir)

os.mkdir('newDir')

import time

time.sleep(3)
os.rename('newDir', 'newDir2')

time.sleep(3)
os.rmdir('newDir2')