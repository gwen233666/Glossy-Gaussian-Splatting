import os
import subprocess

images_path = r"/path/to/your/dataset"
folder_path = os.path.dirname(images_path)

command = f'python convert.py -s {folder_path}'
subprocess.run(command, shell=True)
command = f'python train.py -s {folder_path} --eval'
subprocess.run(command, shell=True)
