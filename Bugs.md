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

## Other
