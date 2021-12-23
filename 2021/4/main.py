import os
import zipfile
import detect_zip_bomb  # mein Modul
import datetime

mirfaelltkeinnameein = []  # mir ist in dem Moment kein Name für die Variable eingefallen xD

start = datetime.datetime.now()
with open("rockyou.txt", errors="ignore") as f:
    passwords = f.read().split("\n")


def extract(filename):
    path = "extracted/" + filename
    if not (detect_zip_bomb.pruefen(path) == False):
        raise Exception
    z = zipfile.ZipFile(path)
    try:
        z.extractall("extracted")
        mirfaelltkeinnameein.append({"file": z, "password": "no password", "filename": filename})
        print({"file": z, "password": "no password", "filename": filename})
    except RuntimeError:
        for pw in passwords:
            if len(pw) >= 96:  # durch den Hinweis wissen wir, dass das Passwort 96 Zeichen lang ist. Bei unbekannter Länge kann dieses if statement auch entfernt werden
                try:
                    z.extractall("extracted", pwd=str.encode(pw))
                    mirfaelltkeinnameein.append({"file": z, "password": pw, "filename": filename})
                    print({"file": z, "password": pw, "filename": filename})
                    break
                except RuntimeError:
                    pass
    except FileNotFoundError:
        print(FileNotFoundError)  # bei einem FileNotFoundError stoppt das Script nicht, sondern macht mit den anderen Zip-Dateien weiter
    os.remove(path)


if __name__ == "__main__":
    while True:
        dirlist = os.listdir("extracted")
        zipcounter = 0
        for i in dirlist:
            if i.endswith(".zip"):
                print("start file " + str(i))
                extract(i)
                zipcounter += 1
        if zipcounter == 0:
            break
    stop = datetime.datetime.now()
    print("Fertig!\nZeit: " + str(stop - start))
    print(mirfaelltkeinnameein)
