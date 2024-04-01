class sorting_normal:
    def __init__(self, file_endings):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            self.sort_files(file_endings)

    def sort_files_normal(self, file_endings):
        self.count_elements = 1
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                continue
            else:
                for key in file_endings:
                    if file.endswith(tuple(file_endings[key])):
                        self.count_elements += 1
                        if not os.path.exists(os.path.join(self.folder_path, key)):
                            os.makedirs(os.path.join(self.folder_path, key))
                        shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                        break
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")

class sorting_subdir:
    def __init__(self, file_endings):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            self.sort_files(file_endings)

    def sort_files_subdir(self, file_endings):
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                sorting_subdir()
            else:
                for key in self.file_ending_:
                    try:
                        if self.file_ending_[key] == []:
                            continue
                        elif file.endswith(tuple(self.file_ending_[key])):
                            if not os.path.exists(os.path.join(self.folder_path, key)):
                                os.makedirs(os.path.join(self.folder_path, key))
                            shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                            self.count_elements += 1
                            break
                    except:
                        pass
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")

class sorting_subdir_subdir:
    def __init__(self, folder_path, file):
        self.folder_path = folder_path
        subfolder = os.path.join(self.folder_path, file)
        if os.path.isdir(os.path.join(subfolders, file)):
            sorting_subdir_subdir(os.path.join(subfolders, file), file)
        for file_sub in os.listdir(subfolder):
            if os.path.isdir(os.path.join(subfolders, file_sub)):
                sorting_subdir_subdir(os.path.join(subfolders, file), file_sub)
            for key in self.file_ending_:
                try:
                    if file_sub.endswith(tuple(self.file_ending_[key])):
                        if not os.path.exists(os.path.join(subfolder, key)):
                            os.makedirs(os.path.join(subfolder, key))
                        shutil.move(os.path.join(subfolder, file_sub), os.path.join(subfolder, key, file_sub))
                        self.count_elements += 1
                        break
                except:
                    pass