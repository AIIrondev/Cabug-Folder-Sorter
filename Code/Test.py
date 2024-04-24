from magika import Magika
import os
import shutil

magika = Magika()
file_path = os.listdir(os.getcwd())

for file in file_path:
    print(file)
    if os.path.isdir(file):
        continue
    if os.path.isfile(file):
        with open(file, "br") as f:
            select = f.read()
            result = magika.identify_bytes(select)
            print(result.output.ct_label)
