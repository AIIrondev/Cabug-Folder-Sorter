from magika import Magika
import os
import shutil

magika = Magika()
file_path = os.listdir(os.getcwd())

for file in file_path:
    print(file)
    if os.path.isdir(file):
        continue
    else:
        with open(os.path.join(file), "br") as f:
            select = f.read()
            result = magika.identify_bytes(select)
            print(result.output.ct_label)
        match result.output.ct_label:
            case "text":
                print(f"{file} is text file")
            case "image":
                print(f"{file} is image file")
            case "audio":
                print(f"{file} is audio file")
            case "video":
                print(f"{file} is video file")
            case "archive":
                print(f"{file} is archive file")
            case "document":
                print(f"{file} is document file")
            case "executable":
                print(f"{file} is executable file")
            case "font":
                print(f"{file} is font file")
            case "code":
                print(f"{file} is code file")
            case "database":
                print(f"{file} is database file")
            case "disk_image":
                print(f"{file} is disk image file")
            case "spreadsheet":
                print(f"{file} is spreadsheet file")
            case "empty":
                print(f"{file} is empty file")
                
                # finisch this code
            
def sort_files_normal_magika(self, file_endings): # TODO: Finisch the magika sorting in version 2.3.0
        magika = Magika()
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        self.count_elements = 1
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                continue
            else:
                result = magika.identify_path(Path(file))
                for key in file_endings_magika:
                    if result.output.ct_label == key:
                        count_file_type_add[key] += 1
                        log.info(f"File: {file}: {key}")
                        self.count_elements += 1
                        count_file_sortet_add += 1
                        if not os.path.exists(os.path.join(self.folder_path, key)):
                            os.makedirs(os.path.join(self.folder_path, key))
                        shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                        break
                    elif key == "Other":
                        count_file_type_add["Other"] += 1
                        log.info(f"File: {file}: Other")
                        if not os.path.exists(os.path.join(self.folder_path, "Other")):
                            os.makedirs(os.path.join(self.folder_path, "Other"))
                        shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, "Other", file))
                        self.count_elements += 1