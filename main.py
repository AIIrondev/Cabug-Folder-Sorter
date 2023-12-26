# import modules
import customtkinter as tk
import tkinter
import PIL as Image
import os
import shutil
import time
import logging
import webbrowser


# Konfigurieren des Loggers
logger = logging.getLogger('folder sorter')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('fs.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# variables
image = False
video = False
object3d = False
document = False
audio = False
executable = False
archive = False
code = False
other = False

# Version 0.1.1 -> first version of the folder sorter
# Version 0.1.2 -> first version of the folder sorter with extra menu final
# Version 1.1.1 -> Versions fix von 0.1.2 -> VErbesserte und effizientere Version und haptisches Featback für bessere User Experience
# Version 1.1.2 -> Einfügung von einem extra menu -> besser für Anfänger
# Version 2.1.1 -> verwendet auch die .py dateien zum ändern der Directorys
# Version 2.1.2 -> verwendet auch die .py dateien zum ändern der Directorys final
# Version 2.2.2 -> Verbessern des Codes und hinzufügen von mehr optionen -> effizienter und schneller
# Version 3.1.1 -> Einfügen von einem File system watcher -> wenn ein neues File in den Ordner kommt wird es automatisch verschoben
# Version 3.1.2 -> Einfügen von einem File system watcher -> wenn ein neues File in den Ordner kommt wird es automatisch verschoben final
# Version 3.2.2 -> Zwei verschiedene Modi -> Normal und Advanced -> besser für Anfänger und Fortgeschrittene
# Version 4.1.1 -> Einführen von einem File system -> umbau auf ein File system -> mit den Funkltionen von v.3.1.2
# Version 4.1.2 -> Einführen von einem File system -> umbau auf ein File system -> mit den Funkltionen von v.3.1.2 final

class GUI:
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("Folder sorter")
        self.window.geometry("275x300")
        self.window.resizable(False, False)
        self.window._set_appearance_mode("light")
        self.main_menu()

    def main_menu(self):
        logger.debug("Opening menu")
        self.first_reset()
        tk.CTkLabel(self.window, text="Folder sorter", font=("Arial", 25), text_color="black").place(x=75, y=0) # set corner to #242424 for dark mode
        tk.CTkButton(self.window, text="Sort folder", corner_radius=32, text_color="black",command=lambda: self.main()).place(x=75, y=100)
        tk.CTkButton(self.window, text="Exit", corner_radius=32, command=self.window.destroy, fg_color="#ff0000", hover_color="#b30000", text_color="black").place(x=75, y=200)
        tk.CTkButton(self.window, text="About", corner_radius=32, command=self.about, text_color="black").place(x=75, y=150)
        tk.CTkLabel(self.window, text="Made by: @AIIrondev", font=("Arial", 10), text_color="black").place(x=90, y=250)
        tk.CTkLabel(self.window, text="Version: 0.1.2", font=("Arial", 10), text_color="black").place(x=100, y=270)

    def main(self):
        logger.debug("Opening main menu")
        self.first_reset()
        tk.CTkLabel(self.window, text="Folder sorter", font=("Arial", 25), text_color="black").place(x=75, y=0)
        tk.CTkButton(self.window, text="Select folder", command=self.select_folder, corner_radius=32, text_color="black").place(x=75, y=70)
        tk.CTkLabel(self.window, text="Mode: ", font=("Arial", 15), text_color="black").place(x=90, y=130)
        tk.CTkOptionMenu(self.window, values=["Normal", "Custom"], command=self.option_calback_menu).place(x=75, y=160)
        tk.CTkButton(self.window, text="Back", corner_radius=32, command=self.main_menu, text_color="black").place(x=75, y=250)
        tk.CTkButton(self.window, text="Start", corner_radius=32, command=lambda: sorting(self.folder_button), text_color="black").place(x=75, y=200)

    def about(self):
        logger.debug("Opening about menu")
        self.first_reset()
        tk.CTkLabel(self.window, text="Folder sorter", font=("Arial", 25), text_color="black").place(x=75, y=0)
        tk.CTkLabel(self.window, text="Made by: @AIIrondev", font=("Arial", 15), text_color="black").place(x=90, y=250)
        tk.CTkButton(self.window, text="LICENCE", text_color="blue", command=lambda: self.open_html_file("li.html"), corner_radius=32).place(x=75, y=100)
        tk.CTkLabel(self.window, text="Version: 0.1.2", font=("Arial", 15), text_color="black").place(x=100, y=270)
        tk.CTkLabel(self.window, text="Github: https://github.com/Iron-witch/Folder-sorter", font=("Arial", 10), text_color="blue").place(x=25, y=50)
        tk.CTkButton(self.window, text="Back", corner_radius=32, command=self.main_menu, text_color="black").place(x=75, y=150)
    
    def select_folder(self):
        logger.debug("Selecting folder")
        self.folder_button = tk.filedialog.askdirectory()

    def first_reset(self, window_size_x=275, window_size_y=300):
        self.clear_window()
        self.window.geometry(f"{window_size_x}x{window_size_y}")
    
    def clear_window(self):
        logger.debug("Clearing window")
        for widget in self.window.winfo_children():
            widget.destroy()
            
    def open_html_file(self, file_path):
        logger.debug("Opening html file")
        # Open the HTML file in the default web browser
        webbrowser.open(file_path)

    def check_var(self):
        pass

    def option_calback_menu(self, value):
        logger.debug("Opening option menu")
        self.first_reset(275, 400)
        self.check_var_img = tk.StringVar(value=False)
        self.check_var_vid = tk.StringVar(value=False)
        self.check_var_3do = tk.StringVar(value=False)
        self.check_var_doc = tk.StringVar(value=False)
        self.check_var_aud = tk.StringVar(value=False)
        self.check_var_exe = tk.StringVar(value=False)
        self.check_var_arc = tk.StringVar(value=False)
        self.check_var_cod = tk.StringVar(value=False)
        self.check_var_oth = tk.StringVar(value=False)
        tk.CTkLabel(self.window, text="Folder sorter", font=("Arial", 25), text_color="black").place(x=75, y=0)
        tk.CTkButton(self.window, text="Select folder", command=self.select_folder, corner_radius=32, text_color="black").place(x=75, y=30)
        tk.CTkOptionMenu(self.window, values=["Normal", "Custom"], command=self.option_calback_menu).place(x=75, y=110)
        tk.CTkButton(self.window, text="Back", corner_radius=32, command=self.main_menu, text_color="black").place(x=75, y=350)
        if value == "Custom": 
            tk.CTkLabel(self.window, text="Custom mode", font=("Arial", 15), text_color="black").place(x=75, y=150)
            tk.CTkCheckBox(self.window, text="Image", variable=self.check_var_img ,onvalue=True, offvalue=False).place(x=50, y=175)
            tk.CTkCheckBox(self.window, text="Video", variable=self.check_var_vid ,onvalue=True, offvalue=False).place(x=50, y=200)
            tk.CTkCheckBox(self.window, text="3D object", variable=self.check_var_3do ,onvalue=True, offvalue=False).place(x=50, y=225)
            tk.CTkCheckBox(self.window, text="Document", variable=self.check_var_doc ,onvalue=True, offvalue=False).place(x=50, y=250)
            tk.CTkCheckBox(self.window, text="Audio", variable=self.check_var_aud ,onvalue=True, offvalue=False).place(x=150, y=175)
            tk.CTkCheckBox(self.window, text="Executable", variable=self.check_var_exe ,onvalue=True, offvalue=False).place(x=150, y=200)
            tk.CTkCheckBox(self.window, text="Archive", variable=self.check_var_arc ,onvalue=True, offvalue=False).place(x=150, y=225)
            tk.CTkCheckBox(self.window, text="Code", variable=self.check_var_cod ,onvalue=True, offvalue=False).place(x=150, y=250)
            tk.CTkCheckBox(self.window, text="Other", variable=self.check_var_oth ,onvalue=True, offvalue=False).place(x=150, y=275)
            tk.CTkButton(self.window, text="Start", corner_radius=32, command=lambda: self.custom_mode_gui(), text_color="black").place(x=75, y=310)
        elif value == "Normal":
            self.main()
    
    def custom_mode_gui(self):
        # get values from check boxes
        global image, video, object3d, document, audio, executable, archive, code, other
        image = self.check_var_img.get()
        video = self.check_var_vid.get()
        object3d = self.check_var_3do.get()
        document = self.check_var_doc.get()
        audio = self.check_var_aud.get()
        executable = self.check_var_exe.get()
        archive = self.check_var_arc.get()
        code = self.check_var_cod.get()
        other = self.check_var_oth.get()
        try:
            sorting(self.folder_button)
        except NameError:
            logger.warning("No folder selected")
            warning = tk.CTkWarning(self.window, text="No folder selected", text_color="black")
      
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
            "other": ["sonsiges"]
        }
        if image or video or object3d or document or audio or executable or archive or code or other:
            self.custom_mode(folder, f"{image},{video},{object3d},{document},{audio},{executable},{archive},{code},{other}")
            logger.debug(f"Starting custom mode with {image},{video},{object3d},{document},{audio},{executable},{archive},{code},{other}")
        else:
            self.sort_ending(folder)
            
    def custom_mode(self, folder, mode):
        # create right table for custom mode
        image, video, object3d, document, audio, executable, archive, code, other = mode.split(",")
        logger.debug("Starting custom mode")
        self.custom_mode_folder_changer = self.ending_folder_changer.copy()
        if image == "False":
            del self.custom_mode_folder_changer["image"]
        if video == "False":
            del self.custom_mode_folder_changer["video"]
        if object3d == "False":
            del self.custom_mode_folder_changer["3d object"]
        if document == "False":
            del self.custom_mode_folder_changer["document"]
        if audio == "False":
            del self.custom_mode_folder_changer["audio"]
        if executable == "False":
            del self.custom_mode_folder_changer["executable"]
        if archive == "False":
            del self.custom_mode_folder_changer["archive"]
        if code == "False":
            del self.custom_mode_folder_changer["code"]
        if other == "False":
            del self.custom_mode_folder_changer["other"]
        logger.debug("Starting sorting")
        for file in os.listdir(folder):
            logger.debug(file)
            file_ending = self.get_file_ending(file)
            if file_ending == False:
                logger.warning("No ending found1 -> moving to other folder")
            else:
                for folder in self.custom_mode_folder_changer:
                    if file_ending in self.custom_mode_folder_changer[folder]:
                        logger.debug("Ending found1 -> moving to folder")
                        self.create_folder(f"{folder}")
                        self.move_file(f"{file}", f"{folder}")
                        break
                else:
                    logger.debug("No ending found3 -> moving to other folder")
        

    def sort_ending(self, ending_folder):
        logger.debug("Sorting endings")
        for file in os.listdir(ending_folder):
            logger.debug(file)
            file_ending = self.get_file_ending(file)
            if file_ending == False:
                logger.warning("No ending found -> moving to other folder")
            else:
                for folder in self.ending_folder_changer:
                    if file_ending in self.ending_folder_changer[folder]:
                        logger.debug("Ending found1 -> moving to folder")
                        self.create_folder(f"{ending_folder}/{folder}")
                        self.move_file(f"{ending_folder}/{file}", f"{ending_folder}/{folder}")
                        break
                else:
                    logger.debug("No ending found2 -> moving to other folder")
                        
    def move_file(self, file, folder):
        file_path = os.path.join(folder, file)
        if os.path.exists(file_path):
            shutil.move(file_path, folder)
        else:
            logger.error(f"File not found: {file_path}")

    def create_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def get_file_ending(self, file):
        return os.path.splitext(file)[1][1:]

if __name__ == "__main__":
    logger.info("Programm gestartet")
    window = GUI()
    window.window.mainloop()
    logger.info("Programm beendet")
