import shutil
import os
import json

def main():
    data = json.load("all_files.json")
    for element in data:
        if element == "conf":
            conf = data[element]
            print(conf)
        if element == "magika":
            magika = data[element]
            print(magika)
        if element == "language":
            language = data[element]
            print(language)
        if element == "help":
            help = data[element]
            print(help)


if __name__ == "__main__":
    main()
    print("Done!")