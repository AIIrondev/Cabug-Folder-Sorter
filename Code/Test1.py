import shutil
import os
import json

file_list = ['file1.json', 'file2.json', 'file3.json']
data = {
    "conf.json": {},
    "magika_conf.json": {},
    "language.json": {},
    "help.json": {},
}


def import_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def export_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    for file in file_list:
        data[file].append(import_json_file(file))
    export_json_file('output.json', data)
        
        
if __name__ == "__main__":
    main()
    print("Done!")