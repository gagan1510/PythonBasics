import os
import time

source = ['/home/gagan/test']

target_dir=['pytest']

target = ''.join(target_dir)+ os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(''.join(target_dir)):
    os.mkdir(''.join(target_dir))

zip_command = 'zip -r {0} {1}'.format(''.join(target), ' '.join(source))

print('Zip command is: ')
print(zip_command)
print('Running::')
if os.system(zip_command) == 0:
    print('Successfully backed up to', target)
else:
    print('backup FAILED')