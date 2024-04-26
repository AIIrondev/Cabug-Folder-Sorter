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
            
