from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
from customtkinter import *
import json


help_loaded = ""
color_background = "#262626"
color_main = "#eda850"
color_help = "white"
conf_file = "Data/conf/all_conf.json"
try:
    with open(conf_file, "r", encoding='utf-8') as f:
        data = json.load(f)
        for element in data:
            if element == "help":
                help_loaded = data[element]
except:
    pass


class help_engine:
    def __init__(self, menuitem):
        self.menu_item = menuitem
        with open(conf_file, "r", encoding='utf-8') as f:
            data = json.load(f)
            for element in data:
                if element == "help":
                    self.help_file = data[element]
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
        self.app.iconbitmap("Data/images/Cabug-folder-sorter.ico")
        self.app.config(bg=color_background)
        self.main_font = CTkFont(family="Helvetica", size=12)
        CTkLabel(self.app, text="Help Catalog", font=("Arial", 20), bg_color=color_background, text_color=color_main).place(x=120, y=10)
        CTkLabel(self.app, text="Select the help you want to see", font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=90, y=50)
        CTkLabel(self.app, text="1. Complete Help", font=("Arial", 12), bg_color=color_background, text_color=color_main).place(x=90, y=90)
        self.app.mainloop()

    def on_closing(self):
        self.app.destroy()