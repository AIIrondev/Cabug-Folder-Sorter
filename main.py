# import modules
import customtkinter as tk
import tkinter
import PIL as Image
import os
import shutil
import time
import logging


# Konfigurieren des Loggers
logger = logging.getLogger('folder sorter')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('fs.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.info("Programm gestartet")

class GUI:
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("Folder sorter")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window._set_appearance_mode("light")
        self.main_menu()

    def main_menu(self):
        logger.debug("Opening menu")
        self.clear_window()
        tk.CTkLabel(self.window, text="Folder sorter", font=("Arial", 25), text_color="blue").place(x=175, y=0) # set corner to #242424 for dark mode
        tk.CTkButton(self.window, text="Sort folder", corner_radius=32, command=lambda: self.main()).place(x=175, y=100)
        tk.CTkButton(self.window, text="Exit", corner_radius=32, command=self.window.destroy, fg_color="#ff0000", hover_color="#b30000").place(x=175, y=150)

    def main(self):
        logger.debug("Opening main menu")
        self.clear_window()
        self.folder_button = None
        tk.CTkLabel(self.window, text="Folder sorter", font=("Arial", 25)).place(x=175, y=0)
        tk.CTkButton(self.window, text="Select folder", command=self.select_folder, corner_radius=32).place(x=175, y=100)
        tk.CTkButton(self.window, text="Back", corner_radius=32, command=self.main_menu).place(x=175, y=150)

    def select_folder(self):
        self.button = tk.filedialog.askdirectory()
        self.folder_button = self.button
        sorting(self.folder_button)
    
    def clear_window(self):
        logger.debug("Clearing window")
        for widget in self.window.winfo_children():
            widget.destroy()

class sorting:
    def __init__(self, folder):
        self.ending_folder_changer = {
            "image": ["jpg", "png", "gif", "jpeg", "bmp"],
            "video": ["mp4", "avi", "mov", "mkv"],
            "3d object": ["obj", "fbx", "3ds", "stl", "dae", "ply", "x3d", "gltf", "glb"],
            "document": ["pdf", "docx", "doc", "txt"],
            "audio": ["mp3", "wav", "ogg", "flac"],
            "executable": ["exe", "msi", "bat", "sh", "jar"],
            "archive": ["zip", "rar", "7z", "tar", "gz", "xz"],
            "code": ["py", "html", "css", "js", "cpp", "c", "java", "h", "hpp", "cs", "php", "json", "xml", "sql", "asm", "asmx", "aspx", "jsp", "vb", "vbs", "rb", "pl", "go", "swift", "kt", "m", "r", "lua", "ts", "tsx", "yml", "yaml", "ini", "cfg", "conf", "md", "markdown", "bat", "cmd", "ps1", "psm1", "psd1", "ps1xml", "psc1", "pssc", "reg", "scf", "scr", "vbs", "ws", "wsf", "wsc", "wsh", "ps2", "ps2xml", "psc2", "pscxml", "cdxml", "xaml", "xaml", "xsl", "xslt", "xsd", "xsc", "xsd", "xsf", "config", "settings", "props", "sln", "csproj", "vbproj", "vcxproj", "vcproj", "dbproj", "njsproj", "vcxitems", "vcxitems", "csproj", "vbproj", "vcxproj", "vcproj", "dbproj", "njsproj", "vcxitems", "vcxitems", "vcxitems", "proj", "projitems", "shproj", "manifest", "appxmanifest"],
        }
        self.sort_ending(folder)

    def sort_ending(self, ending_folder):
        logger.debug("Sorting endings")
        for file in os.listdir(ending_folder):
            for folder in self.ending_folder_changer:
                for ending in self.ending_folder_changer[folder]:
                    if ending == self.get_file_ending(file):
                        self.create_folder(folder)
                        self.move_file(file, folder)
                        logger.debug("File moved")
                    else:
                        logger.debug("File not moved")
        
    def move_file(self, file, folder):
        os.system(f"move {file} {folder}")

    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.system(f"mkdir {folder}")
            logger.debug("Folder created")
        else:
            logger.debug("Folder already exists")

    def get_file_ending(self, file):
        for i in range(len(file)):
            if file[i] == ".":
                return file[i:]
                logger.debug("Ending found")
            else:
                logger.warning("No ending found")
                return False

if __name__ == "__main__":
    window = GUI()
    window.window.mainloop()
