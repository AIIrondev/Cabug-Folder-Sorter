# Bugs

## List of Bug categories

1. [Cosmetic](#cosmetic)
2. [Functional](#functional)
3. [User interface](#user-interface)
4. [Critical](#critical)
5. [Unimportant](#unimportant)
6. [Others](#other)

## Cosmetic

### Icons in customtkinter/tkinter 0.1.2.1

If you want to use an icon in a customtkinter/tkinter project and for it to look good you have to remove the background.

## Functional

### Fixed version file directory 0.1.2.2

Before:

```python
__version__ = "?"
with open("version", "r") as f:
    __version__ = f.read()
```

After:

```python
__version__ = "?"
try:
    with open("version", "r") as f:
        __version__ = f.read()
except:
    pass
```

### Atributte error 0.1.2.3

This is an error where I acidently try'd to use the `_path_exist` function from the `os` library wich doesent exist.

Before:

```python
def __init__(self):
    self.folder_path = folder_to_sort
    if self.folder_path == "":
        print("Please select a folder")
    elif os.dir(self.folder_path):
        self.sort_files()
```

After:

```python
def __init__(self):
    self.folder_path = folder_to_sort
    if self.folder_path == "":
        print("Please select a folder")
    elif os.path.exists(self.folder_path):
        self.sort_files()
```

### Error while sorting files 1.1.1.1

This error accured while sorting files in a folder, and the key was not defined.

Before:

```python
def sort_files(self):
    self.prepare()
    for file in os.listdir(self.folder_path):
        if os.path.isdir(os.path.join(self.folder_path, file)):
            continue
        else:
            for key in self.file_ending_:
                if self.file_ending_[key] == []:
                    pass
                elif file.endswith(tuple(self.file_ending_)):
                    self.count_elements += 1
                    if not os.path.exists(os.path.join(self.folder_path, key)):
                        os.makedirs(os.path.join(self.folder_path, key))
                    shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                    break
    messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")
```

After:

```python
def sort_files(self):
    self.prepare()
    for file in os.listdir(self.folder_path):
        if os.path.isdir(os.path.join(self.folder_path, file)):
            continue
        else:
            for key in self.file_ending_:
                if self.file_ending_[key] == []:
                    pass
                elif file.endswith(tuple(self.file_ending_[key])):
                    try:
                        if not os.path.exists(os.path.join(self.folder_path, key)):
                            os.makedirs(os.path.join(self.folder_path, key))
                        shutil.move(os.path.join(self.folder_path, file), os.path.join(self.folder_path, key, file))
                        self.count_elements += 1
                        break
                    except:
                        pass
    messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")
```

### TypeError: 'sort_advanced_script' object is not callable 1.2.2.4

This Error accurred because I named a class and a function out of a nother class the same way.

Before:

```python
def sort_advanced_script(self):
    self.reset()
    self.folder_path = StringVar()
    self.folder_path.set("")
    self.conf_file = StringVar()
    self.conf_file.set("")
    CTkLabel(self.root, text="Cabug Folder Sorter Advanced", text_color="blue", font=("Arial", 20)).place(x=70, y=10)
    CTkButton(self.root, text="Select Folder", command=self.browse, corner_radius=10).place(x=140, y=50)
    CTkButton(self.root, text="Select Config File", command=self.browse_conf_file, corner_radius=10).place(x=140, y=100)
    CTkButton(self.root, text="Sort", command=sort_advanced_script(self.folder_path.get(), self.conf_file.get()), corner_radius=10).place(x=140, y=150)
    CTkButton(self.root, text="Main Menu", command=self.menu, corner_radius=10, fg_color="Red", hover_color="Darkred").place(x=140, y=300)
    CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
    CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=370)
```

After:

```python
def sort_advanced_menu_script(self):
    self.reset()
    self.folder_path = StringVar()
    self.folder_path.set("")
    self.conf_file = StringVar()
    self.conf_file.set("")
    CTkLabel(self.root, text="Cabug Folder Sorter Advanced", text_color="blue", font=("Arial", 20)).place(x=70, y=10)
    CTkButton(self.root, text="Select Folder", command=self.browse, corner_radius=10).place(x=140, y=50)
    CTkButton(self.root, text="Select Config File", command=self.browse_conf_file, corner_radius=10).place(x=140, y=100)
    CTkButton(self.root, text="Sort", command=sort_advanced_script(self.folder_path.get(), self.conf_file.get()), corner_radius=10).place(x=140, y=150)
    CTkButton(self.root, text="Main Menu", command=self.menu, corner_radius=10, fg_color="Red", hover_color="Darkred").place(x=140, y=300)
    CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
    CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=370)
```

## User Interface

### `str` object is not callable for habtic featback 1.2.2.4

THis will acurre when you call an `str` as a function.

Before:

```python
messagebox.INFO("finisched sorting", f"Finisched sorting of {self.count_elements} elements \n in the folder {self.folder_path}.")
```

After:

```python
messagebox.showinfo("Folder Sorter",f"Finisched sorting of {str(self.count_elements)} elements \n in the folder {folder_to_sort}.")
```

### _tkinter.TclError: image "option.png" doesn't exist 1.2.2.5

I dont know why this error accurred but the fix for it was to us another library -> PIL

Before:

```python
def menu(self):
    self.reset()
    heeight = 70
    wieght = 240
    CTkButton(self.root, image="option.png", text="", command=self.menu_options, corner_radius=15).place(x=0, y=0)
    CTkLabel(self.root, text="Cabug Folder Sorter", text_color="blue", font=("Arial", 20)).place(x=120, y=10)
    CTkLabel(self.root, text="Select a mode", text_color="black", font=("Arial", 12)).place(x=165, y=50)
    CTkButton(self.root, text="Simple Mode", command=self.simple_mode, corner_radius=15, width=wieght, height=heeight).place(x=90, y=90)
    CTkButton(self.root, text="Advanced Mode", command=self.sort_advanced_menu, corner_radius=15, width=wieght, height=heeight).place(x=90, y=170)
    CTkButton(self.root, text="Exit", command=self.on_closing, corner_radius=15, fg_color="Red", hover_color="Darkred", width=140, height=60).place(x=140, y=250)
    CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
    CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=370)
```

After:

```python
def menu(self):
    self.option_image = CTkImage(light_image=Image.open("option.png"),size=(30, 30))
    self.reset()
    heeight = 70
    wieght = 240
    CTkButton(self.root, image=self.option_image, text="", command=self.menu_options).place(x=0, y=0)
    CTkLabel(self.root, text="Cabug Folder Sorter", text_color="blue", font=("Arial", 20)).place(x=120, y=10)
    CTkLabel(self.root, text="Select a mode", text_color="black", font=("Arial", 12)).place(x=165, y=50)
    CTkButton(self.root, text="Simple Mode", command=self.simple_mode, corner_radius=15, width=wieght, height=heeight).place(x=90, y=90)
    CTkButton(self.root, text="Advanced Mode", command=self.sort_advanced_menu, corner_radius=15, width=wieght, height=heeight).place(x=90, y=170)
    CTkButton(self.root, text="Exit", command=self.on_closing, corner_radius=15, fg_color="Red", hover_color="Darkred", width=140, height=60).place(x=140, y=250)
    CTkLabel(self.root, text=f"© Maximilian Gründinger 2024", text_color="Blue",font=("Arial", 9)).place(x=150, y=350)
    CTkLabel(self.root, text=f"Version {__version__}", text_color="Blue",font=("Arial", 9)).place(x=185, y=370)
```

## Critical

## Unimportant

### Unintentional creating a new window 1.0.1.1

This accured while reseting my screen for a new Menu.

Before:

```python
def reset(self):
    for widget in self.root.winfo_children():
        widget.destroy()
    self.root.geometry("400x420")
    self.root.resizable(False, False)
    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.root.iconbitmap("Cabug-folder-sorter.ico")
```

After:

```python
def reset(self):
    for widget in self.root.winfo_children():
        widget.destroy()
```

### Changed `print` to `messagebox` 1.2.2.5

This was just a improvement for the response to the User.

Before:

```python
if self.folder_path == "":
    print("Please select a folder")
elif os.path.exists(self.folder_path):
    self.sort_files()
```

After:

```python
if self.folder_path == "":
    messagebox.showerror("Folder Sorter", "Please select a folder")
elif os.path.exists(self.folder_path):
    self.sort_files()
```

## Other


### AttributeError: `app` object has no attribute `Images` 1.2.2.3

This Error accurred because I was building a new Menu for Script sorting / Checkbox sorting, because the names where uncleare -> have to rework the names.

Before:

```python
def sort_advanced_menu(self):
    self.reset()
    CTkLabel(self.root, text="Cabug Folder Sorter Advanced", text_color="blue", font=("Arial", 20)).place(x=70, y=10)
    CTkLabel(self.root, text="Select the Mode you want", text_color="black", font=("Arial", 12)).place(x=90, y=50)
    CTkButton(self.root, text="Sort with Config File", command=self.sort_advanced_script, corner_radius=15, width=240, height=70).place(x=90, y=90)
    CTkButton(self.root, text="Sort with Checkboxes", command=self.sort_advanced, corner_radius=15, width=240, height=70).place(x=90, y=170) # <- Error with the name
```

After:

```python
def sort_advanced_menu(self):
    self.reset()
    CTkLabel(self.root, text="Cabug Folder Sorter Advanced", text_color="blue", font=("Arial", 20)).place(x=70, y=10)
    CTkLabel(self.root, text="Select the Mode you want", text_color="black", font=("Arial", 12)).place(x=90, y=50)
    CTkButton(self.root, text="Sort with Config File", command=self.sort_advanced_script, corner_radius=15, width=240, height=70).place(x=90, y=90)
    CTkButton(self.root, text="Sort with Checkboxes", command=self.advanced_mode, corner_radius=15, width=240, height=70).place(x=90, y=170) # <- changed the name to right one
```