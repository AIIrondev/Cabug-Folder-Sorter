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

## Other
