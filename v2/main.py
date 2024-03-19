#folder sorter
import os
import shutil
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox


# Global Variables
folder_to_sort = ""
__version__ = "0.0.0.1"


# Classes
class app:
    def __init__(self):
        self.root = CTk()
        self.root.title("Folder Sorter")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        # self.root.iconbitmap("icon.ico") # Design real icon for version 1.0.0.0

        self.folder_path = StringVar()
        self.folder_path.set("")
        
        CTkLabel(self.root, text="Folder Sorter", text_color="blue", font=("Arial", 20)).place(x=150, y=10)
        CTkLabel(self.root, text=f"&copy Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).pack(pady=10)
        CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue").pack(pady=10)
        self.root.mainloop()
        
    def browse(self):
        global folder_to_sort
        folder_to_sort = filedialog.askdirectory()
        self.folder_path.set(folder_to_sort)
        

class sort:
    def __init__(self):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            messagebox.showerror("Error", "Please select a folder")
        else:
            self.folder = os.listdir(self.folder_path)
        
        

if __name__ == "__main__":
    app()