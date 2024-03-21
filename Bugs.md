# Bugs

## List of Bug categories

1. [Cosmetic](#cosmetic)
2. [Functional](#functional)
3. [User interface](#user-interface)
4. [Critical](#critical)
5. [Unimportant](#unimportant)
6. [Others](#other)

## Cosmetic

### Icons in customtkinter/tkinter

If you want to use an icon in a customtkinter/tkinter project and for it to look good you have to remove the background.

## Functional

### Fixed version file directory

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

## User Interface

## Critical

## Unimportant

## Other
