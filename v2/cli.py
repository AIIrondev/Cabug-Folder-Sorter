# imports
import click
import os
import sys
import shutil

# Global Variables
folder_to_sort = ""
__version__ = "0.0.0.1"
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


with open("version", "r") as f:
    __version__ = f.read()


# Functions
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


# CLI
@click.command()
@click.argument("folder", type=click.Path(exists=True))
@click.version_option(__version__, "--version", "-v", help="Show version", prog_name="Folder Sorter")
@click.help_option("--help", "-h", help="Show this help message and exit")
def cli(folder):
    try:
        global folder_to_sort
        folder_to_sort = folder
        sort()
        click.echo(f"Successfully sortet {folder}.")

    except Exception as e:
        click.echo(f"Error: An error occurred during sorting. {str(e)}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    cli()
