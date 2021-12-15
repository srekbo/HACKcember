#!/usr/bin/env python3
import os
import zipfile as zf
import sys
from tkinter import filedialog


def get_size(filename):
    zip_file = zf.ZipFile(filename)
    return sum([file.file_size for file in zip_file.filelist]) / 1024 ** 3


def pruefen(filename, threshold=5, ratio=10, raiseexception=True):
    size = round(get_size(filename), 2)
    if size > threshold:
        if raiseexception:
            raise Exception("File is potential ZIP bomb ({} GB)!".format(size))
        else:
            print("File is potential ZIP bomb ({} GB)!".format(size))
    zip_size = os.path.getsize(filename) / 1024 ** 3
    ratio2 = int(round(size / zip_size, 0))
    if ratio2 > ratio:
        if raiseexception:
            raise Exception("File is potential ZIP bomb (ratio {}:1)!".format(ratio2))
        else:
            print("File is potential ZIP bomb (ratio {}:1)!".format(ratio2))
    return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if pruefen(sys.argv[1], raiseexception=False):
            print("Alles Klar")
    else:
        print("Verwendung:\ndetect_zip_bomb.py <dateiname>")
        input_filename = filedialog.askopenfilename(initialdir="./", title="Bild auswählen", filetypes=(("ZIP-files", "*.zip"), ("all files", "*.*")))
        if pruefen(input_filename, raiseexception=False):
            print("Alles Klar")
