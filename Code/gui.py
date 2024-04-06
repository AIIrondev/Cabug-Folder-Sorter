#folder sorter
import os
import shutil
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox
import json
from PIL import Image


# Global Variables
folder_to_sort = ""
conf_file = ""
subfolders = ""
language = "en"
__version__ = "1.0.1.1"
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
        self.main_font = CTkFont(family="Helvetica", size=12)
        self.root.config(bg="#262626")
        global button_sub_sort
        button_sub_sort = BooleanVar() # The value of the checkbox that decides if the subfolders should be sorted or not
        # Template: CTkButton(,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626")
        self.menu()
        self.root.mainloop()

    def menu(self):
        self.option_image = CTkImage(light_image=Image.open("option.png"),size=(40, 40))
        self.reset()
        heeight = 70
        wieght = 240
        CTkButton(self.root, image=self.option_image, text="", command=self.menu_options, width=20, height=20, bg_color="#262626", fg_color="#262626", hover_color="#262626",border_color="#262626").place(x=0, y=0) # make the button look like the image with out borders
        CTkLabel(self.root, text="Cabug Folder Sorter", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=120, y=10)
        CTkLabel(self.root, text="Select a mode", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=165, y=60)
        CTkButton(self.root, text="Simple Mode", command=self.simple_mode, width=wieght, height=heeight,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=90, y=90)
        CTkButton(self.root, text="Advanced Mode", command=self.sort_advanced_menu, width=wieght, height=heeight, font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=90, y=170)
        CTkButton(self.root, text="?", command=lambda:self.help("simple_main"),width=15, height=20, bg_color="#262626",fg_color= "#262626",hover=True, hover_color="#262626", border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=330, y=110)
        CTkButton(self.root, text="?", command=lambda:self.help("advanced_main"),width=15, height=20, bg_color="#262626",fg_color= "#262626",hover=True, hover_color="#262626", border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=330, y=190)
        CTkButton(self.root, text="Exit", command=self.on_closing, width=140, height=60, font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color="Red", bg_color="#262626",fg_color= "#262626").place(x=140, y=250)
        CTkLabel(self.root, text="by Maximilian Gründinger 2024",font=("Arial", 9), bg_color="#262626", text_color="#eda850").place(x=150, y=40)

    def menu_options(self):
        self.reset()
        CTkLabel(self.root, text="Cabug Folder Sorter", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=120, y=10)
        CTkButton(self.root, text="About", command=self.about,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=50)
        CTkButton(self.root, text="Help", command=self.help_complete,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=100)
        CTkLabel(self.root, text="Select a language", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=150, y=150)
        CTkButton(self.root, text="English", command=self.menu,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=190) # TODO: Add language Models
        CTkButton(self.root, text="Deutsch", command=self.menu,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=220)
        CTkCheckBox(self.root, text="Sort Subfolders", variable=button_sub_sort, bg_color="#262626", text_color="#eda850").place(x=140, y=250)
        CTkButton(self.root, text="Main Menu", command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color="#262626",fg_color= "#262626").place(x=140, y=300)
        CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="#eda850",font=("Arial", 9), bg_color="#262626").place(x=150, y=350)
        CTkLabel(self.root, text=f"Version {__version__}", text_color="#eda850",font=("Arial", 9), bg_color="#262626").place(x=185, y=370)

    def simple_mode(self):
        self.reset()
        self.folder_path = StringVar()
        self.folder_path.set("")
        CTkLabel(self.root, text="Cabug Folder Sorter Basic", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=90, y=10)
        CTkButton(self.root, text="Select Folder", command=self.browse,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=50)
        CTkButton(self.root, text="Sort", command=sort,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=100)
        CTkButton(self.root, text="Main Menu", command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color="#262626",fg_color= "#262626").place(x=140, y=300)

    def sort_advanced_menu(self):
        self.reset()
        heeight = 70
        wieght = 240
        CTkLabel(self.root, text="Cabug Folder Sorter Advanced", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=70, y=10)
        CTkLabel(self.root, text="Select the Mode you want", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=90, y=50)
        CTkButton(self.root, text="Sort with Config File", command=self.sort_advanced_menu_script, width=wieght, height=heeight,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=90, y=90)
        CTkButton(self.root, text="Sort with Checkboxes", command=self.advanced_mode, width=wieght, height=heeight,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=90, y=170)
        CTkButton(self.root, text="Main Menu", command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color="#262626",fg_color= "#262626").place(x=140, y=300)

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
        CTkLabel(self.root, text="Cabug Folder Sorter Advanced", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=70, y=10)
        CTkButton(self.root, text="Select Folder", command=self.browse,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=50)
        # Checkboxes
        CTkCheckBox(self.root, text="Images", variable=self.Images, bg_color="#262626", text_color="#eda850").place(x=X_position_1, y=100)
        CTkCheckBox(self.root, text="Videos", variable=self.Videos, bg_color="#262626", text_color="#eda850").place(x=X_position_2, y=100)
        CTkCheckBox(self.root, text="Audio", variable=self.Audio, bg_color="#262626", text_color="#eda850").place(x=X_position_1, y=130)
        CTkCheckBox(self.root, text="Documents", variable=self.Documents, bg_color="#262626", text_color="#eda850").place(x=X_position_2, y=130)
        CTkCheckBox(self.root, text="Archives", variable=self.Archives, bg_color="#262626", text_color="#eda850").place(x=X_position_1, y=160)
        CTkCheckBox(self.root, text="3D Models", variable=self.Models, bg_color="#262626", text_color="#eda850").place(x=X_position_2, y=160)
        CTkCheckBox(self.root, text="PCB", variable=self.PCB, bg_color="#262626", text_color="#eda850").place(x=X_position_1, y=190)
        CTkCheckBox(self.root, text="Code", variable=self.Code, bg_color="#262626", text_color="#eda850").place(x=X_position_2, y=190)
        CTkCheckBox(self.root, text="Executables", variable=self.Executables, bg_color="#262626", text_color="#eda850").place(x=X_position_1, y=220)
        CTkCheckBox(self.root, text="Fonts", variable=self.Fonts, bg_color="#262626", text_color="#eda850").place(x=X_position_2, y=220)
        CTkCheckBox(self.root, text="Other", variable=self.Other, bg_color="#262626", text_color="#eda850").place(x=X_position_1, y=250)
        # Buttons
        CTkButton(self.root, text="Sort", command=self.sort_advanced,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=310)
        CTkButton(self.root, text="Main Menu", command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color="#262626",fg_color= "#262626").place(x=140, y=340)

    def sort_advanced_menu_script(self):
        self.reset()
        self.folder_path = StringVar()
        self.folder_path.set("")
        self.conf_file = StringVar()
        self.conf_file.set("")
        CTkLabel(self.root, text="Cabug Folder Sorter Advanced", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=70, y=10)
        CTkButton(self.root, text="Select Folder", command=self.browse,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=50)
        CTkButton(self.root, text="Select Config File", command=self.browse_conf_file,font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=100)
        CTkButton(self.root, text="Sort", command=lambda: sort_advanced_script(self.folder_path.get(), self.conf_file.get()),font=self.main_font,text_color="#eda850",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "#eda850", bg_color="#262626",fg_color= "#262626").place(x=140, y=150)
        CTkButton(self.root, text="Main Menu", command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color="#262626",fg_color= "#262626").place(x=140, y=300)

    def help_complete(self):
        self.reset()
        CTkLabel(self.root, text="Help", font=("Arial", 20), bg_color="#262626", text_color="#eda850").place(x=120, y=10)
        CTkLabel(self.root, text="To use Folder Sorter, select the option that you want to sort.", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=50)
        CTkLabel(self.root, text="After that select the folder you want to sort and click the 'Sort' button.", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=80)
        CTkLabel(self.root, text="The program will then sort the files in the folder.", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=110)
        CTkLabel(self.root, text="To use the Advanced Checkbox Mode, select the folder you want to sort ", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=140)
        CTkLabel(self.root, text="and select the options you want to sort.", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=170)
        CTkLabel(self.root, text="The program will then sort the files in the folder.", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=170)
        CTkLabel(self.root, text="If you want to sort with a config file, select the folder you want to sort", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=200)
        CTkLabel(self.root, text="and select the config file you want to use.", font=("Arial", 12), bg_color="#262626", text_color="#eda850").place(x=10, y=230)
        CTkButton(self.root, text="Main Menu", command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color="#262626",fg_color= "#262626").place(x=140, y=300)

    def sort_advanced(self):
        advanced_sort(self.Images.get(), self.Videos.get(), self.Audio.get(), self.Documents.get(), self.Archives.get(), self.Models.get(), self.PCB.get(), self.Code.get(), self.Executables.get(), self.Fonts.get(), self.Other.get())

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def about(self):
        messagebox.showinfo("About", "Folder Sorter is a simple program to sort your files in a folder. It is developed by Maximilian Gründinger")

    def help_Basic(self):
        messagebox.showinfo("Help", "To use Folder Sorter, select the folder you want to sort and click the 'Sort' button. The program will then sort the files in the folder.")

    def help_Advanced(self):
        messagebox.showinfo("Help", f"To use Folder Sorter, select the folder you want to sort and click the 'Sort' button, after you have selectet the Options you want to sort. The program will then sort the files in the folder.")

    def help(self, menuitem):
        help_engine(menuitem)

    def browse(self):
        global folder_to_sort
        folder_to_sort = filedialog.askdirectory()
        self.folder_path.set(folder_to_sort)

    def browse_conf_file(self):
        global conf_file
        conf_file = filedialog.askopenfilename()
        self.conf_file.set(conf_file)

    def reset(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            

class help_engine:
    def __init__(self, menuitem):
        self.menu_item = menuitem
        self.help_complete()

    def help_complete(self):
        match self.menu_item:
            case "help":
                self.help_catalog(1)
            case "simple_main":
                self.help_catalog(2)
            case "advanced_main":
                self.help_catalog(3)
            case "sel_language":
                self.help_catalog(4)
            case "sort_file_menu":
                self.help_catalog(5)
            case "sort_check_menu":
                self.help_catalog(6)
            case "select_simple":
                self.help_catalog(7)
            case "select_advanced_script":
                self.help_catalog(8)
            case "select_advanced_script_conf":
                self.help_catalog(9)
            case "select_advanced_check":
                self.help_catalog(10)
            case "sort_simple":
                self.help_catalog(11)
            case "sort_advanced_script":
                self.help_catalog(12)
            case "sort_advanced_check":
                self.help_catalog(13)
            case "sort_subdir":
                self.help_catalog(14)
                
    def help_catalog(self, case_number): # gets the right help message from a .json file and displays it
        pass
    
    def on_closing(self):
        self.root.destroy()


class language_engine: # returns the right language part for the requestet language and part
    def __init__(self, part):
        self.language = language
        self.set_language()
    
    def set_language(self):
        pass


class sort:
    def __init__(self):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            if button_sub_sort:
                sorting_subdir(self.folder_path)
            else:
                sort_files_normal(self.folder_path)

class sort_advanced_script: # get file ending dict as .json file
    def __init__(self, folder, conf_file):
        self.folder = folder
        self.conf_file = conf_file
        with open(conf_file, "r") as f:
            file_ending_conf = json.load(f)
        if self.folder == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder):
            if button_sub_sort:
                sorting_subdir(self.folder)
            else:
                sort_files_normal(self.folder)

    def sort_advanced(self):
        self.count_elements = 1
        
        for file in os.listdir(self.folder):
            if os.path.isdir(os.path.join(self.folder, file)):
                continue
            else:
                for key in file_ending_conf:
                    if file.endswith(tuple(file_ending_conf[key])):
                        self.count_elements += 1
                        if not os.path.exists(os.path.join(self.folder, key)):
                            os.makedirs(os.path.join(self.folder, key))
                        shutil.move(os.path.join(self.folder, file), os.path.join(self.folder, key, file))
                        break
        messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {self.folder}.")

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
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            self.prepare()
            if button_sub_sort:
                sorting_subdir(self.folder_path)
            else:
                sort_files_normal(self.folder_path)

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
        

class sorting_normal:
    def __init__(self, file_endings):
        self.folder_path = folder_to_sort
        if self.folder_path == "":
            messagebox.showerror("Folder Sorter", "Please select a folder")
        elif os.path.exists(self.folder_path):
            sort_files_normal(file_endings)

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



if __name__ == "__main__":
    app()