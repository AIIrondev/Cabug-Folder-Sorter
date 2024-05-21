import shutil
import os
import json

def main():
    data = json.load("all_files.json")
    for element in data:
        if element == "conf":
            conf = data[element]
        if element == "magika":
            magika = data[element]
        if element == "language":
            language = data[element]
        if element == "help":
            help = data[element]


if __name__ == "__main__":
    main()
    print("Done!")