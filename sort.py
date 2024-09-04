import os
import shutil
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import json
from PIL import Image
import zipfile
import matplotlib.pyplot as plt
import logging as log
from magika import Magika
import threading
from sort import *
from help import help_engine as help_engine

class sort:
    def __init__(self):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            count_folder_sortet_add += 1
            log.info("Folder")
            if button_sub_sort.get():
                sorting_subdir(self.folder_path, file_ending)
            else:
                sorting_normal( file_ending)


class sort_advanced_script: # get file ending dict as .json file
    def __init__(self, folder, conf_file):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        self.folder = folder
        self.conf_file = conf_file
        with open(conf_file, "r") as f:
            file_ending_conf = json.load(f)
        if self.folder == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder):
            count_folder_sortet_add += 1
            log.info("Folder")
            if button_sub_sort.get():
                sorting_subdir(self.folder, file_ending_conf)
            else:
                sorting_normal(file_ending_conf)


class advanced_sort:
    def __init__(self, Images, Videos, Audio, Documents, Archives, Models, PCB, Code, Executables, Fonts, Other):
        self.folder_path = folder_to_sort
        self.Images = Images
        self.Videos = Videos
        self.Audio = Audio
        self.Documents = Documents
        self.Archives = Archives
        self.Models = Models
        self.PCB = PCB
        self.Code = Code
        self.Executables = Executables
        self.Fonts = Fonts
        self.Other = Other
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            self.prepare()
            count_folder_sortet_add += 1
            log.info("Folder")
            if button_sub_sort.get():
                sorting_subdir(self.folder_path, self.file_ending_)
            else:
                sorting_normal(self.file_ending_)

    def prepare(self):
        self.file_ending_ = {
            "Images": [],
            "Videos": [],
            "Audio": [],
            "Documents": [],
            "Archives": [],
            "3D Models": [],
            "PCB": [],
            "Code": [],
            "Executables": [],
            "Fonts": [],
            "Other": []
        }
        if self.Images:
            self.file_ending_["Images"] = file_ending["Images"]
        if self.Videos:
            self.file_ending_["Videos"] = file_ending["Videos"]
        if self.Audio:
            self.file_ending_["Audio"] = file_ending["Audio"]
        if self.Documents:
            self.file_ending_["Documents"] = file_ending["Documents"]
        if self.Archives:
            self.file_ending_["Archives"] = file_ending["Archives"]
        if self.Models:
            self.file_ending_["3D Models"] = file_ending["3D Models"]
        if self.PCB:
            self.file_ending_["PCB"] = file_ending["PCB"]
        if self.Code:
            self.file_ending_["Code"] = file_ending["Code"]
        if self.Executables:
            self.file_ending_["Executables"] = file_ending["Executables"]
        if self.Fonts:
            self.file_ending_["Fonts"] = file_ending["Fonts"]
        if self.Other:
            self.file_ending_["Other"] = file_ending["Other"]


class sorting_magika:
    def __init__(self, file_endings):
        self.folder_path = folder_to_sort
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            self.sort_files_magika(file_endings)

    def sort_files_magika(self, file_endings):
        pass

class sorting_normal:
    def __init__(self, file_endings):
        self.folder_path = folder_to_sort
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            if button_magika:
                self.sort_files_normal_magika(file_endings)
            else:
                self.sort_files_normal(file_endings)

    def sort_files_normal(self, file_endings):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        self.count_elements = 1
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                if not os.listdir(file_path):
                    ask = messagebox.showinfo("Folder Sorter",f"Folder {file_path} is empty and will be deleted.")
                    if ask:
                        os.rmdir(file_path)
                continue
            else:
                for key in file_endings:
                    if file.endswith(tuple(file_endings[key])):
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
                        count_file_sortet_add += 1
                        break
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")

    def sort_files_normal_magika(self, file_endings):
        magika = Magika()
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        self.count_elements = 1
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                if not os.listdir(file_path):
                    ask = messagebox.showinfo("Folder Sorter",f"Folder {file_path} is empty and will be deleted.")
                    if ask:
                        os.rmdir(file_path)
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
                        count_file_sortet_add += 1
                        break
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")


class sorting_subdir:
    def __init__(self, folder_path, file_endings):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        self.count_elements = 1
        self.folder_path = folder_path
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            match file_endings:
                case "Images":
                    pass
                case "Videos":
                    pass
                case "Audio":
                    pass
                case "Documents":
                    pass
                case "Archives":
                    pass
                case "3D Models":
                    pass
                case "PCB":
                    pass
                case "Code":
                    pass
                case "Executables":
                    pass
                case "Fonts":
                    pass
                case "Other":
                    pass
                case _:
                    self.sort_files_subdir(file_endings)

    def sort_files_subdir(self, file_endings):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isdir(file_path):
                if not os.listdir(file_path):
                    ask = messagebox.showinfo("Folder Sorter",f"Folder {file_path} is empty and will be deleted.")
                    if ask:
                        os.rmdir(file_path)
                sorting_subdir(file_path, file_endings)
            else:
                for key in file_endings:
                    try:
                        if file_endings[key] == []:
                            continue
                        elif file.endswith(tuple(file_endings[key])):
                            count_file_type_add[key] += 1
                            log.info(f"File: {file}: {key}")
                            if not os.path.exists(os.path.join(self.folder_path, key)):
                                os.makedirs(os.path.join(self.folder_path, key))
                            shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                            self.count_elements += 1
                            count_file_sortet_add += 1
                            break
                        elif key == "Other":
                            count_file_type_add["Other"] += 1
                            log.info(f"File: {file}: Other")
                            if not os.path.exists(os.path.join(self.folder_path, "Other")):
                                os.makedirs(os.path.join(self.folder_path, "Other"))
                            shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, "Other", file))
                            self.count_elements += 1
                            count_file_sortet_add += 1
                            break
                    except:
                        pass
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")

    def sort_files_subdir_magika(self, file_endings):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isdir(file_path):
                if not os.listdir(file_path):
                    ask = messagebox.showinfo("Folder Sorter",f"Folder {file_path} is empty and will be deleted.")
                    if ask:
                        os.rmdir(file_path)
                sorting_subdir(file_path, file_endings)
            else:
                for key in file_endings:
                    try:
                        if file_endings[key] == []:
                            continue
                        elif file.endswith(tuple(file_endings[key])):
                            count_file_type_add[key] += 1
                            log.info(f"File: {file}: {key}")
                            if not os.path.exists(os.path.join(self.folder_path, key)):
                                os.makedirs(os.path.join(self.folder_path, key))
                            shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                            self.count_elements += 1
                            count_file_sortet_add += 1
                            break
                        elif key == "Other":
                            count_file_type_add["Other"] += 1
                            log.info(f"File: {file}: Other")
                            if not os.path.exists(os.path.join(self.folder_path, "Other")):
                                os.makedirs(os.path.join(self.folder_path, "Other"))
                            shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, "Other", file))
                            self.count_elements += 1
                            count_file_sortet_add += 1
                            break
                    except:
                        pass
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")

