import shutil
import os
import json

conf_file = "all_conf.json"

def main():
    with open(conf_file, "r", encoding='utf-8') as f:
        data = json.load(f)
    for element in data:
        if element == "conf":
            conf = data[element]
            print(conf)
            print("")
            print(conf["version"])
            print("")
        if element == "magika":
            magika = data[element]
            print(magika)
            print("")
            print(magika['Images'])
            print("")
        if element == "language":
            language = data[element]
            print(language)
            print("")
            print(language['en'])
            print("")
        if element == "help":
            help = data[element]
            print(help)
            print("")
            print(help['Simple Menu Help'])
            print("")


if __name__ == "__main__":
    main()