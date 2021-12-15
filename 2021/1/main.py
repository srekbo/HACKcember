import os
import zipfile
import detect_zip_bomb
import datetime

start = datetime.datetime.now()


def extract(filename):
    path = "extracted/" + filename
    if not (detect_zip_bomb.pruefen(path) == False):
        raise Exception
    try:
        with zipfile.ZipFile(path) as z:
            z.extractall("extracted")
    except FileNotFoundError:
        print(FileNotFoundError)
    os.remove(path)


if __name__ == "__main__":
    while True:
        dirlist = os.listdir("extracted")
        zipcounter = 0
        for i in dirlist:
            if i.endswith(".zip"):
                extract(i)
                zipcounter += 1
        if zipcounter == 0:
            break
    stop = datetime.datetime.now()
    print(stop-start)