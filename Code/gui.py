#folder sorter
import os
import shutil
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox


# Global Variables
folder_to_sort = ""
__version__ = "0.1.2.1"
file_ending = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico"],
    "Videos": [".mp4", ".mkv", ".webm", ".flv", ".avi", ".mov", ".wmv", ".mpg", ".mpeg", ".3gp", ".3g2"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma", ".aac", ".aiff", ".alac", ".dsd"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".csv", ".xml", ".json", ".html", ".htm", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".lz", ".lzma", ".lzo", ".zst", ".tz", ".cab", ".arj", ".lzh", ".ace", ".uue", ".bz", ".jar", ".iso", ".img", ".dmg", ".vhd", ".vmdk", ".vdi", ".qcow", ".qcow2"],
    "3D Models": [".stl", ".obj", ".fbx", ".blend", ".3ds", ".dae", ".ply", ".lwo", ".lws", ".lxl", ".lxo", ".ac", ".ase", ".dxf", ".dwf", ".ifc", ".kmz", ".wrl", ".x3d", ".x3db", ".x3dv", ".x3dz"],
    "PCB": [".brd", ".sch", ".pcb", ".pcbdoc", ".brd", ".sch", ".pcb", ".pcbdoc", ".fzz", ".fz", ".gbr", ".gbl", ".gbo", ".gbp", ".gbs", ".gml", ".gko", ".gtp", ".gts", ".gto"],
    "Code": [".py", ".c", ".cpp", ".h", ".hpp", ".java", ".js", ".ts", ".html", ".css", ".php", ".go", ".rs", ".rb", ".swift", ".kt", ".dart", ".lua", ".sh", ".bat", ".ps1", ".psm1", ".psd1", ".ps1xml", ".pssc", ".psc1", ".pssc", ".psh", ".pash", ".pasm", ".pas", ".pl", ".pm", ".tcl", ".r", ".cs", ".vb", ".vbs", ".vba", ".vbscript", ".vbe", ".vbs"],
    "Executables": [".exe", ".msi", ".apk", ".app", ".bat", ".com", ".gadget", ".jar", ".wsf", ".sh", ".bash", ".csh", ".zsh", ".fish", ".ps1", ".psm1", ".psd1", ".ps1xml", ".pssc", ".psc1", ".pssc", ".psh", ".pash", ".pasm", ".pas", ".pl", ".pm", ".tcl", ".r", ".cs", ".vb", ".vbs", ".vba", ".vbscript", ".vbe", ".vbs"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot", ".svg", ".svgz", ".dfont", ".pfa", ".pfb", ".pfm", ".afm", ".cid", ".cff", ".otc", ".t42", ".t11", ".fon", ".fnt", ".woff", ".woff2", ".eot", ".svg", ".svgz", ".dfont", ".pfa", ".pfb", ".pfm", ".afm", ".cid", ".cff", ".otc", ".t42", ".t11", ".fon", ".fnt"],
    "Other": [".*"]
}


try:
    with open("version", "r") as f:
        __version__ = f.read()
except:
    pass

# Classes
class app:
    def __init__(self):
        self.root = CTk()
        self.root.title("Folder Sorter")
        self.root.geometry("400x420")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.iconbitmap("Cabug-folder-sorter.ico")
        self.menu()
        self.root.mainloop()

    def menu(self):
        self.reset()
        heeight = 70
        wieght = 240
        CTkLabel(self.root, text="Cabug Folder Sorter", text_color="blue", font=("Arial", 20)).place(x=120, y=10)
        CTkLabel(self.root, text="Select a mode", text_color="black", font=("Arial", 12)).place(x=165, y=50)
        CTkButton(self.root, text="Simple Mode", command=self.simple_mode, corner_radius=15, width=wieght, height=heeight).place(x=90, y=90)
        CTkButton(self.root, text="Advanced Mode", command=self.advanced_mode, corner_radius=15, width=wieght, height=heeight).place(x=90, y=170)
        CTkButton(self.root, text="Exit", command=self.on_closing, corner_radius=15, fg_color="Red", hover_color="Darkred", width=140, height=60).place(x=140, y=250)
        CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
        CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=370)

    def simple_mode(self):
        self.reset()
        self.folder_path = StringVar()
        self.folder_path.set("")

        CTkLabel(self.root, text="Cabug Folder Sorter Basic", text_color="blue", font=("Arial", 20)).place(x=90, y=10)
        CTkButton(self.root, text="Select Folder", command=self.browse, corner_radius=10).place(x=140, y=50)
        CTkButton(self.root, text="Sort", command=sort, corner_radius=10).place(x=140, y=100)
        CTkButton(self.root, text="Help", command=self.help, corner_radius=10).place(x=140, y=150)
        CTkButton(self.root, text="Main Menu", command=self.menu, corner_radius=10, fg_color="Red", hover_color="Darkred").place(x=140, y=300)
        CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
        CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=370)

    def advanced_mode(self):
        self.reset()
        # Variables
        self.folder_path = StringVar()
        self.folder_path.set("")
        self.Images = BooleanVar()
        self.Videos = BooleanVar()
        self.Audio = BooleanVar()
        self.Documents = BooleanVar()
        self.Archives = BooleanVar()
        self.Models = BooleanVar()
        self.PCB = BooleanVar()
        self.Code = BooleanVar()
        self.Executables = BooleanVar()
        self.Fonts = BooleanVar()
        self.Other = BooleanVar()
        # Checkboxes positions
        X_position_1 = 120
        X_position_2 = 220
        # Headline
        CTkLabel(self.root, text="Cabug Folder Sorter Advanced", text_color="blue", font=("Arial", 20)).place(x=70, y=10)
        CTkButton(self.root, text="Select Folder", command=self.browse, corner_radius=10).place(x=140, y=50)
        # Checkboxes
        CTkCheckBox(self.root, text="Images", variable=self.Images).place(x=X_position_1, y=100)
        CTkCheckBox(self.root, text="Videos", variable=self.Videos).place(x=X_position_2, y=100)
        CTkCheckBox(self.root, text="Audio", variable=self.Audio).place(x=X_position_1, y=130)
        CTkCheckBox(self.root, text="Documents", variable=self.Documents).place(x=X_position_2, y=130)
        CTkCheckBox(self.root, text="Archives", variable=self.Archives).place(x=X_position_1, y=160)
        CTkCheckBox(self.root, text="3D Models", variable=self.Models).place(x=X_position_2, y=160)
        CTkCheckBox(self.root, text="PCB", variable=self.PCB).place(x=X_position_1, y=190)
        CTkCheckBox(self.root, text="Code", variable=self.Code).place(x=X_position_2, y=190)
        CTkCheckBox(self.root, text="Executables", variable=self.Executables).place(x=X_position_1, y=220)
        CTkCheckBox(self.root, text="Fonts", variable=self.Fonts).place(x=X_position_2, y=220)
        CTkCheckBox(self.root, text="Other", variable=self.Other).place(x=X_position_1, y=250)
        # Buttons
        CTkButton(self.root, text="Help", command=self.help, corner_radius=10).place(x=140, y=280)
        CTkButton(self.root, text="Sort", command=self.sort_advanced, corner_radius=10).place(x=140, y=310)
        CTkButton(self.root, text="Main Menu", command=self.menu, corner_radius=10, fg_color="Red", hover_color="Darkred").place(x=140, y=340)
        CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=370)
        CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=390)

    def sort_advanced(self):
        self.reset()
        CTkLabel(self.root, text="Advanced Mode", text_color="blue", font=("Arial", 20)).place(x=150, y=10)
        CTkLabel(self.root, text="Select the file types you want to sort", text_color="black", font=("Arial", 12)).place(x=100, y=50)

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

    def reset(self):
        for widget in self.root.winfo_children():
            widget.destroy()


class sort:
    def __init__(self):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            print("Please select a folder")
        elif os.path.exists(self.folder_path):
            self.sort_files()

    def sort_files(self):
        self.count_elements = 1
        for file in os.listdir(self.folder_path):
            if os.path.isdir(os.path.join(self.folder_path, file)):
                continue
            else:
                for key in file_ending:
                    if file.endswith(tuple(file_ending[key])):
                        self.count_elements += 1
                        if not os.path.exists(os.path.join(self.folder_path, key)):
                            os.makedirs(os.path.join(self.folder_path, key))
                        shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                        break
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")


if __name__ == "__main__":
    app()