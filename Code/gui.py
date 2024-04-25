# Cabug Folder Sorter
import os
import shutil
from customtkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import json
from PIL import Image
import matplotlib.pyplot as plt
import logging as log
from magika import Magika
import threading

# sertup logging
log.basicConfig(filename="folder_sorter.log", level=log.DEBUG, format="%(asctime)s - %(message)s")

# Global Variables
folder_to_sort = ""
help_file = "help.json"
language_file = "language.json"
subfolders = ""
conf_file = "conf.json"
sort_subdir = False
stat_file = "statistics.json"
button_magika = False
__language__ = "en"
__version__ = "1.0.1.1"
color_background = "#262626"
color_main = "#eda850"
color_help = "white"
count_file_sortet_add = 0
count_folder_sortet_add = 0
count_file_type_add = {}
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
file_endings_magika = {
    "Images": ["Image"],
    "Videos": ["Video"],
    "Audio": ["Audio"],
    "Documents": ["Document"],
    "Archives": ["Archive"],
    "3D Models": ["3D Model"],
    "PCB": ["PCB"],
    "Code": ["Code"],
    "Executables": ["Executable"],
    "Fonts": ["Font"],
    "Other": [".*"]
    
}


try:
    with open(conf_file, "r") as f:
        json_file = json.load(f)
        version = json_file["version"]
        __version__ = version
        sort_subdir = json_file["sort_subdir"]
        color_background = json_file["color_background"]
        color_main = json_file["color_main"]
        __language__ = json_file["active_lang"]
        sort_magika = json_file["sort_magika"]
except:
    pass

# Classes
class app:
    def __init__(self):
        self.root = CTk()
        self.root.title("Cabug Folder Sorter")
        self.root.geometry("400x420")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.iconbitmap("Cabug-folder-sorter.ico")
        self.main_font = CTkFont(family="Helvetica", size=12)
        self.root.config(bg=color_background)
        global button_sub_sort
        global button_stat_sort
        global button_magika
        button_sub_sort = BooleanVar()
        button_stat_sort = BooleanVar()
        button_magika = BooleanVar()
        # Template: CTkButton(,font=self.main_font,text_color_background=color_main,hover=True,hover_color_background="black",border_width=2,corner_radius=3,border_color_background= color_main, bg_color_background=color_background,fg_color_background= color_background)
        self.menu() 
        self.root.mainloop()

    def menu(self):
        if button_stat_sort.get():
            statistics.initialise()
        self.option_image = CTkImage(light_image=Image.open("option.png"),size=(40, 40))
        self.reset()
        heeight = 70
        wieght = 240
        CTkButton(self.root, image=self.option_image, text="", command=self.menu_options, width=20, height=20, bg_color=color_background, fg_color=color_background, hover_color=color_background,border_color=color_background).place(x=0, y=0) # make the button look like the image with out borders
        CTkLabel(self.root, text="Cabug Folder Sorter", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=120, y=10)
        CTkLabel(self.root, text=language_engine(0), font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=165, y=60)
        CTkButton(self.root, text=language_engine(1), command=self.simple_mode, width=wieght, height=heeight,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=90, y=90)
        CTkButton(self.root, text=language_engine(2), command=self.sort_advanced_menu, width=wieght, height=heeight, font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=90, y=170)
        CTkButton(self.root, text="?", command=lambda:self.help("simple_main"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=340, y=115)
        CTkButton(self.root, text="?", command=lambda:self.help("advanced_main"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=340, y=195)
        CTkButton(self.root, text=language_engine(3), command=self.on_closing, width=140, height=60, font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color="Red", bg_color=color_background,fg_color= color_background).place(x=140, y=250)
        CTkLabel(self.root, text="by Maximilian Gründinger 2024",font=("Arial", 9), bg_color=color_background, text_color=color_main).place(x=150, y=40)
        button_sub_sort.get()

    def menu_options(self):
        self.reset()
        CTkLabel(self.root, text="Cabug Folder Sorter", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=120, y=10)
        CTkButton(self.root, text=language_engine(4), command=self.about,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=50)
        CTkButton(self.root, text="Help", command=lambda:self.help("help"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=80)
        CTkLabel(self.root, text="Select a language", font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=150, y=120)
        CTkButton(self.root, text="?", command=lambda:self.help("sel_language"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=270, y=120)
        CTkButton(self.root, text="Language Menu", command=lambda:self.language_menu(),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=150)
        CTkButton(self.root, text="Color Menu", command=lambda:self.color_menu(),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=180)
        CTkButton(self.root, text="Statistics", command=self.statistics,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=210)
        CTkCheckBox(self.root, text=language_engine(5), variable=button_sub_sort, bg_color=color_background, text_color=color_main).place(x=140, y=300)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_subdir"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=270, y=300)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=330)
        CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color=color_main,font=("Arial", 9), bg_color=color_background).place(x=150, y=370)
        CTkLabel(self.root, text=f"Version {__version__}", text_color=color_main,font=("Arial", 9), bg_color=color_background).place(x=185, y=390)
        button_sub_sort.get()

    def simple_mode(self):
        self.reset()
        self.folder_path = StringVar()
        self.folder_path.set("")
        CTkLabel(self.root, text=language_engine(28), font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=90, y=10)
        CTkButton(self.root, text=language_engine(7), command=self.browse,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=50)
        CTkButton(self.root, text="?", command=lambda:self.help("select_simple"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=55)
        CTkButton(self.root, text=language_engine(8), command=sort,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=100)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_simple"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=100)
        CTkCheckBox(self.root, text=language_engine(5), variable=button_sub_sort, bg_color=color_background, text_color=color_main).place(x=140, y=200)
        CTkCheckBox(self.root, text="sort with magika", variable=button_magika, bg_color=color_background, text_color=color_main).place(x=140, y=230)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=300)

    def sort_advanced_menu(self):
        self.reset()
        heeight = 70
        wieght = 240
        CTkLabel(self.root, text=language_engine(12), font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=70, y=10)
        CTkLabel(self.root, text=language_engine(9), font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=90, y=50)
        CTkButton(self.root, text=language_engine(10), command=self.sort_advanced_menu_script, width=wieght, height=heeight,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=90, y=90)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_file_menu"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=340, y=115)
        CTkButton(self.root, text=language_engine(11), command=self.advanced_mode, width=wieght, height=heeight,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=90, y=170)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_check_menu"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=340, y=195)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=300)

    def advanced_mode(self):
        self.reset()
        self.ask_sort_subdir()
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
        CTkLabel(self.root, text=language_engine(13), font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=70, y=10)
        CTkButton(self.root, text=language_engine(7), command=self.browse,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=50)
        CTkButton(self.root, text="?", command=lambda:self.help("select_advanced_check"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=54)
        # Checkboxes
        CTkCheckBox(self.root, text=language_engine(14), variable=self.Images, bg_color=color_background, text_color=color_main).place(x=X_position_1, y=100)
        CTkCheckBox(self.root, text=language_engine(15), variable=self.Videos, bg_color=color_background, text_color=color_main).place(x=X_position_2, y=100)
        CTkCheckBox(self.root, text=language_engine(16), variable=self.Audio, bg_color=color_background, text_color=color_main).place(x=X_position_1, y=130)
        CTkCheckBox(self.root, text=language_engine(17), variable=self.Documents, bg_color=color_background, text_color=color_main).place(x=X_position_2, y=130)
        CTkCheckBox(self.root, text=language_engine(18), variable=self.Archives, bg_color=color_background, text_color=color_main).place(x=X_position_1, y=160)
        CTkCheckBox(self.root, text=language_engine(19), variable=self.Models, bg_color=color_background, text_color=color_main).place(x=X_position_2, y=160)
        CTkCheckBox(self.root, text=language_engine(20), variable=self.PCB, bg_color=color_background, text_color=color_main).place(x=X_position_1, y=190)
        CTkCheckBox(self.root, text=language_engine(21), variable=self.Code, bg_color=color_background, text_color=color_main).place(x=X_position_2, y=190)
        CTkCheckBox(self.root, text=language_engine(22), variable=self.Executables, bg_color=color_background, text_color=color_main).place(x=X_position_1, y=220)
        CTkCheckBox(self.root, text=language_engine(23), variable=self.Fonts, bg_color=color_background, text_color=color_main).place(x=X_position_2, y=220)
        CTkCheckBox(self.root, text=language_engine(24), variable=self.Other, bg_color=color_background, text_color=color_main).place(x=X_position_1, y=250)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_advanced_check_box"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=X_position_2, y=250)
        # Buttons
        CTkButton(self.root, text=language_engine(8), command=self.sort_advanced,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=310)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_advanced_check"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=315)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=340)
        self.ask_sort_subdir()

    def sort_advanced_menu_script(self):
        self.reset()
        self.folder_path = StringVar()
        self.folder_path.set("")
        self.conf_file = StringVar()
        self.conf_file.set("")
        CTkLabel(self.root, text=language_engine(25), font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=70, y=10)
        CTkButton(self.root, text=language_engine(7), command=self.browse,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=50)
        CTkButton(self.root, text="?", command=lambda:self.help("select_advanced_script"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=55)
        CTkButton(self.root, text=language_engine(26), command=self.browse_conf_file,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=100)
        CTkButton(self.root, text="?", command=lambda:self.help("select_advanced_script_conf"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=100)
        CTkButton(self.root, text=language_engine(8), command=lambda: sort_advanced_script(self.folder_path.get(), self.conf_file.get()),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=150)
        CTkButton(self.root, text="?", command=lambda:self.help("sort_advanced_script"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=290, y=150)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=300)
        self.ask_sort_subdir()

    def language_menu(self):
        self.reset()
        CTkLabel(self.root, text="Language Menu", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=130, y=10)
        CTkLabel(self.root, text="Please select the language you want to use:", font=("Arial", 16), bg_color=color_background, text_color=color_main).place(x=50, y=40)
        CTkButton(self.root, text="English", command=lambda:self.language_change("en"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=70, y=100)
        CTkButton(self.root, text="Deutsch", command=lambda:self.language_change("de"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=70, y=130)
        CTkButton(self.root, text="spanisch", command=lambda:self.language_change("es"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=210, y=100)
        CTkButton(self.root, text="japanese", command=lambda:self.language_change("ja"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=210, y=130)
        CTkButton(self.root, text="Svedisch", command=lambda:self.language_change("sv"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=210, y=130)
        CTkButton(self.root, text="portugiesisch", command=lambda:self.language_change("pt"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=210, y=130)
        CTkButton(self.root, text="russian", command=lambda:self.language_change("ru"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=210, y=130)
        CTkButton(self.root, text="französisch", command=lambda:self.language_change("fr"),font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=210, y=130)
        CTkButton(self.root, text="?", command=lambda:self.help("language menu"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=200, y=260)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=300)

    def color_menu(self):
        self.reset()
        CTkLabel(self.root, text="Color Menu", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=130, y=10)
        CTkLabel(self.root, text="Please select the color you want to use:", font=("Arial", 16), bg_color=color_background, text_color=color_main).place(x=50, y=40)
        CTkButton(self.root, text="Select Background color", command=self.select_color_background,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=100)
        CTkButton(self.root, text="Select Text color", command=self.select_main_color,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=130)
        CTkButton(self.root, text="Reset Colors", command=self.reset_colors,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=160)
        CTkButton(self.root, text="?", command=lambda:self.help("color_menu"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=200, y=260)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=340)

    def statistics(self):
        self.reset()
        CTkLabel(self.root, text="Statistics", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=130, y=10)
        CTkLabel(self.root, text="Here will be the statistics", font=("Arial", 16), bg_color=color_background, text_color=color_main).place(x=50, y=40)
        CTkButton(self.root, text="generate statistics", command=statistics.generate,font=self.main_font,text_color=color_main,hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= color_main, bg_color=color_background,fg_color= color_background).place(x=140, y=100)
        CTkCheckBox(self.root, text="Activate Statistics", variable=button_stat_sort, bg_color=color_background, text_color=color_main).place(x=140, y=150)
        CTkButton(self.root, text="?", command=lambda:self.help("statistics"),width=15, height=20, bg_color=color_background,fg_color= color_background,hover=True, hover_color=color_background, border_color="white", text_color="white",font=self.main_font,border_width=1,corner_radius=32).place(x=200, y=260)
        CTkButton(self.root, text=language_engine(6), command=self.menu,font=self.main_font,text_color="red",hover=True,hover_color="black",border_width=2,corner_radius=3,border_color= "red", bg_color=color_background,fg_color= color_background).place(x=140, y=300)

    def select_color_background(self):
        try:
            color_background = askcolor()[1]
            self.color_background = color_background
            self.root.config(bg=color_background)
            if self.color_background == None:
                color_background = "#262626"
            with open(conf_file, "w") as f:
                json.dump({"version": __version__, "sort_subdir": button_sub_sort.get(), "color_background": color_background, "color_main": color_main}, f)
        except:
            pass

    def select_main_color(self):
        try:
            color_main = askcolor()[1]
            color_background = color_main
            self.root.config(bg=color_background)
            if color_main == None:
                color_main = "#eda850"
            with open(conf_file, "w") as f:
                json.dump({"version": __version__, "sort_subdir": button_sub_sort.get(), "color_background": color_background, "color_main": color_main}, f)
        except:
            pass

    def ask_sort_subdir(self):
        if button_sub_sort.get():
            pass
        else:
            ask = messagebox.askyesno("Folder Sorter", "Do you want to sort the subfolders too?")
            if ask:
                button_sub_sort.set(True)

    def reset_colors(self):
        color_background = "#262626"
        color_main = "#eda850"
        self.root.config(bg=color_background)
        with open(conf_file, "w") as f:
            json.dump({"version": __version__, "sort_subdir": button_sub_sort.get(), "color_background": color_background, "color_main": color_main}, f)

    def sort_advanced(self):
        advanced_sort(self.Images.get(), self.Videos.get(), self.Audio.get(), self.Documents.get(), self.Archives.get(), self.Models.get(), self.PCB.get(), self.Code.get(), self.Executables.get(), self.Fonts.get(), self.Other.get())

    def on_closing(self):
        if messagebox.askokcancel("Quit",language_engine(27)):
            self.root.destroy()

    def about(self):
        messagebox.showinfo("About", "Folder Sorter is a simple program to sort your files in a folder. It is developed by Maximilian Gründinger")

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

    def language_change(self, language):
        global __language__
        __language__ = language

    def __del__(self):# save on closing
        with open(conf_file, "w") as f:
            json.dump({"version": __version__, "sort_subdir": button_sub_sort.get(), "color_background": color_background, "color_main": color_main, "active_lang": __language__, "stats": button_stat_sort.get(),  "sort_magika": button_magika}, f)


class statistics:
    def __init__(self):
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        if button_stat_sort.get():
            if os.path.exists(stat_file):
                self.load()
            else:
                self.initialise()
            with open(stat_file, "r") as f:
                self.stat_file = json.load(f)
            self.count_folder_sortet = self.stat_file["count_folder_sortet"]
            self.count_file_sortet = self.stat_file["count_file_sortet"]
            self.count_file_type = self.stat_file["count_file_type"]
        else:
            pass

    def save(self):
        self.count_file_sortet += count_file_sortet_add
        self.count_folder_sortet += count_folder_sortet_add
        for i in count_file_type_add:
            if i in self.count_file_type:
                self.count_file_type[i] += count_file_type_add[i]
            else:
                self.count_file_type[i] = count_file_type_add[i]
        with open(stat_file, "w") as f:
            json.dump({"count_folder_sortet": self.count_folder_sortet, "count_file_sortet": self.count_file_sortet, "count_file_type": self.count_file_type}, f)

    def load_log(self):
        pass

    def load(self):
        with open(stat_file, "r") as f:
            self.stat_file = json.load(f)
        self.count_folder_sortet = self.stat_file["count_folder_sortet"]
        self.count_file_sortet = self.stat_file["count_file_sortet"]
        self.count_file_type = self.stat_file["count_file_type"]

    def generate():
        plt.figure()

        file_types, counts = zip(*count_file_type.items())
        plt.plot(file_types, counts, marker='o', linestyle='-')
        plt.title('File Types')
        plt.xlabel('Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        plt.savefig("stats_file_types.png")
        
        plt.plot(count_folder_sortet, count_file_sortet, marker='o', linestyle='-')
        plt.title('Folder and File Count')
        plt.xlabel('Folder')
        plt.ylabel('File')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        plt.savefig("stats_folder_file.png")

    def initialise():
        with open(stat_file, "w") as f:
            json.dump({"count_folder_sortet": 0, "count_file_sortet": 0, "count_file_type": {"Images": 0, "Videos": 0}}, f) # append the statistics to the file


class help_engine:
    def __init__(self, menuitem):
        self.menu_item = menuitem
        self.help_file = {}
        with open(help_file, "r") as f:
            self.help_file = json.load(f)
        self.help_complete()

    def help_complete(self):
        match self.menu_item:
            case "help":
                self.help_catalog(1)
            case "simple_main":
                self.help_get("Simple Menu Help")
            case "advanced_main":
                self.help_get("Advanced Menu Help")
            case "sel_language":
                self.help_get("Select Language Help")
            case "sort_file_menu":
                self.help_get("Sort with Config File Menu Help")
            case "sort_check_menu":
                self.help_get("Sort with Checkboxes Menu Help")
            case "select_simple":
                self.help_get("Select Folder Help")
            case "select_advanced_script":
                self.help_get("Select Folder Advanced script Help")
            case "select_advanced_script_conf":
                self.help_get("Select Config File Help")
            case "select_advanced_check":
                self.help_get("Select Advanced Checkbox Folder Help")
            case "sort_simple":
                self.help_get("Sort Simple Help")
            case "sort_advanced_script":
                self.help_get("Sort with Config File Help")
            case "sort_advanced_check":
                self.help_get("Sort with Checkboxes Help")
            case "sort_subdir":
                self.help_get("Sort Subfolders Help")
            case "sort_advanced_check_box":
                self.help_get("Checkboxes Help")
            case "language menu":
                self.help_get("Language Menu Help")
            case "color_menu":
                self.help_get("Color Menu Help")
            case "statistics":
                self.help_get("Statistics Help")

    def help_get(self, help_key):
        messagebox.showinfo(help_key, self.help_file[help_key])

    def help_catalog(self, case_number): # TODO: Finisch this in version 3.0.1.1
        self.app = CTk()
        self.app.title("Help Catalog")
        self.app.geometry("400x420")
        self.app.resizable(False, False)
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.app.iconbitmap("Cabug-folder-sorter.ico")
        self.app.config(bg=color_background)
        self.main_font = CTkFont(family="Helvetica", size=12)
        CTkLabel(self.app, text="Help Catalog", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=120, y=10)
        CTkLabel(self.app, text="Select the help you want to see", font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=90, y=50)
        CTkLabel(self.app, text="1. Complete Help", font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=90, y=90)
        self.app.mainloop()

    def on_closing(self):
        self.app.destroy()


def language_engine(part):
    with open(language_file, "r", encoding='utf-8') as f: 
        language_import = {}
        language_import = json.load(f)
        language_active = language_import[__language__]
        language_active = language_active[part]
        return language_active


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

    def sort_files_subdir_magika(self, file_endings): # TODO: Finisch the magika sorting in version 2.3.0
        global count_file_sortet_add, count_folder_sortet_add, count_file_type_add
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isdir(file_path):
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



if __name__ == "__main__":
    app()
