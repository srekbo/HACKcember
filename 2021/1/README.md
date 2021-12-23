# Challenge 1: Santas Geschenk

Zum Video geht es [hier](https://youtu.be/G3vLQP5yAKQ) und zur Erklärung auf der Website [hier](https://www.floriandalwigk.de/santas-geschenk-hackcember-1/).

## Beschreibung (von der Website)

Da heute der 1. Dezember ist und wir uns erstmal an die Vorweihnachtszeit gewöhnen müssen, habe ich den Weihnachtsmann oder besser gesagt seine fleißigen Helferelfen darum gebeten, mein Geschenk an dich auf eine ganz besondere Art und Weise zu verpacken. Deshalb ist es nicht einmal, nicht zweimal, nicht hundertmal, nicht tausendmal, nicht zweitausendmal, sondern ganze 2021 mal verpackt. Ich dachte mir, dass das einem dem 2021. Geburtstag Jesu Christi angemessene Zahl an Geschenkverpackungen ist, findest du nicht?

Deine Aufgabe besteht darin, mein Geschenk an dich auszupacken und das Passwort zu finden, mit dem du dir das folgende Hacking-Video anschauen kannst

## Was ist zu tun?

Das Geschenk muss ausgepackt werden. Das heißt, dass 2021 mal eine ZIP-Datei entpackt werden muss.

Python hat für den Umgang mit ZIP-Dateien ein Paket mit dem Namen [zipfile](https://docs.python.org/3/library/zipfile.html).

## Lösung

Die Lösung ist in der Datei "main.py".

Erklärung zu der Datei detect_zip_bomb.py gibt es bei [diesem Video](https://youtu.be/t340PxXXMmE). Die Datei kannst du ignorieren, wenn du das Script nur für Dateien verwendest, die aus vertrauenswürdigen Quellen stammen.

<details>
  <summary>Für die Erklärung hier klicken</summary>
  
  Das Script enthält folgende Module:
  1. os: Zum Entfernen der ausgepackten Zip-Dateien und zum Anzeigen von Ordnerinhalten
  2. zipfile: Zum Entpacken der Zip-Dateien
  3. optional - detect_zip_bomb: Eigenes Modul zum Erkennen von Zip-Bomben
  4. optional - datetime bzw. time: Zum Messen der Zeit zwischen start und stop des Scripts
  
  ```python3
  import os
  import zipfile
  import detect_zip_bomb # optional
  import datetime # optional
  ```
  Nach dem Import muss eine Funktion definiert werden, die die Zip-Datei entpackt.
  Diese Funktion...
  1. bekommt als Parameter den Dateinamen der aktuellen Zip-Datei übergeben,
  2. (optional) prüft, ob es sich bei der Datei um eine Zip-Bombe handelt,
  3. entpackt die Zip-Datei und
  4. löscht die alte Datei.
  Im Code sieht das dann so aus:
  ```python3
  def extract(filename):
      path = "extracted/" + filename
      if not (detect_zip_bomb.pruefen(path) == False): # optional
          raise Exception # optional
      try:
          with zipfile.ZipFile(path) as z: # öffnet die Zip-Datei und speichert dies in der Variable z
              z.extractall("extracted") # entpackt die Datei in den Ordner extracted/
              os.remove(path) # entfernt die alte Datei nach dem Entpacken
      except FileNotFoundError:
          print(FileNotFoundError) # bei einem FileNotFoundError stoppt das Script nicht, sondern macht mit den anderen Zip-Dateien weiter
  ```
  Die Funktion ist definiert und muss nur noch aufgerufen werden.
  Das Script soll nun alle Zip-Dateien im Ordner extracted/ entpacken und danach löschen.
  ```python3
  if __name__ == "__main__": # wenn das Script nicht importiert wird sondern ausgeführt wird
      while True: # Endlosschleife
          dirlist = os.listdir("extracted") # speichert den Inhalt des Ordners
          zipcounter = 0 # Zähler der Zip-Dateien
          for file in dirlist: # für jede Datei in dem Ordner
              if file.endswith(".zip"): # wenn der Dateiname mit ".zip" endet
                  extract(file) # ruft die oben definierte Funktion extract() auf und übergibt die Datei
                  zipcounter += 1 # Zählt bei jeder Zip-Datei einmal hoch
          if zipcounter == 0: # wenn es keine Zip-Datei im Ordner gibt
              break # Endlosschleife unterbrechen
  ```
  Viel Spaß beim Ausprobieren!
</details>