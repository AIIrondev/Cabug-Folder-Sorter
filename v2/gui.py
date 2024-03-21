#folder sorter
import os
import shutil
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox


# Global Variables
folder_to_sort = ""
__version__ = "0.0.0.0"

with open("version", "r") as f:
    __version__ = f.read()

# Classes
class app:
    def __init__(self):
        self.root = CTk()
        self.root.title("Folder Sorter")
        self.root.geometry("400x420")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # self.root.iconbitmap("icon.ico") # Design real icon for version 1.0.0.0

        self.folder_path = StringVar()
        self.folder_path.set("")

        CTkLabel(self.root, text="Folder Sorter", text_color="blue", font=("Arial", 20)).place(x=150, y=10)
        CTkButton(self.root, text="Select Folder", command=self.browse, corner_radius=10).place(x=140, y=50)
        CTkButton(self.root, text="Sort", command=sort, corner_radius=10).place(x=140, y=100)
        CTkButton(self.root, text="Help", command=self.help, corner_radius=10).place(x=140, y=150)
        CTkButton(self.root, text="About", command=self.about, corner_radius=10).place(x=140, y=200)
        CTkButton(self.root, text="Exit", command=self.on_closing, corner_radius=10, fg_color="Red", hover_color="Darkred").place(x=140, y=250)
        CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
        CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=190, y=370)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def about(self):
        messagebox.showinfo("About", "Folder Sorter is a simple program to sort your files in a folder. It is developed by Maximilian Gründinger")

    def help(self):
        messagebox.showinfo("Help", "To use Folder Sorter, select the folder you want to sort and click the 'Sort' button. The program will then sort the files in the folder.")

    def browse(self):
        global folder_to_sort
        folder_to_sort = filedialog.askdirectory()
        self.folder_path.set(folder_to_sort)


class sort:
    def __init__(self):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            print("Please select a folder")
        elif os._path_exists(self.folder_path):
            self.sort_files()

    def sort_files(self):
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                continue
            else:
                for key in file_ending:
                    print(key)
                    if file.endswith(tuple(file_ending[key])):
                        if not os.path.exists(os.path.join(self.folder_path, key)):
                            os.makedirs(os.path.join(self.folder_path, key))
                        shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                        break


if __name__ == "__main__":
    app()