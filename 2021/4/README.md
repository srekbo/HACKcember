# Challenge 4: Das LETZTE GESCHENK

Zum Video geht es [hier](https://youtu.be/pe5K5C8zzb4) und zur Erklärung auf der Website [hier](https://www.floriandalwigk.de/das-letzte-geschenk-hackcember-2021).

Die Zip-Datei in dem Ordner extracted/ ist von der oben verlinkten Website

## Beschreibung (von der Website)

Erinnerst du dich noch an den [Anfang des HACKcembers](https://www.floriandalwigk.de/santas-geschenk-hackcember-1/) zurück? Da hast du eine 2021 mal verzippte Datei entweder händisch oder mit einem kleinen Python-Skript entpacken müssen. Wenn du ein Apple-Jünger bis wird sich diese Challenge für dich als ziemlicher Reinfall entpuppt haben, da beim Klicken auf das Geschenk automatisch _alles_ ausgepackt wird. Sorry dafür.

Damit das dieses Mal nicht passiert, habe ich das Geschenk nur einmal verpacken lassen, dafür aber mit einer extrem robusten Folie, die sich nur mit einem bestimmten Passwort öffnen lässt. Mach dir keine Hoffnungen: Das wirst du weder erraten, noch bruteforcen können, da es sehr viele Stellen besitzt, nämlich exakt viermal so viele wie ein Adventskalender Türchen hat. Die einzige Hoffnung besteht evtl. darin, einen Wörterbuchangriff auf die ZIP-Datei zu starten. Ich empfehle dir zum Knacken die berühmt berüchtigte [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt). 

## Was ist zu tun?

Das Geschenk muss ausgepackt werden. Das heißt, dass das Passwort für die Zip-Datei gefunden werden muss. Ich habe hier mein Script von der 1. Challenge genommen und eine kleine weitere Funktion eingebaut.

Python hat für den Umgang mit ZIP-Dateien ein Paket mit dem Namen [zipfile](https://docs.python.org/3/library/zipfile.html).

## Lösung

Die Lösung ist in der Datei "main.py".<br>(die [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) ladet ihr am besten selbst herunter)

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
  Als nächstes wird die Passwort-Datei "rockyou.txt" eingelesen:
  ```python3
  with open("rockyou.txt", errors="ignore") as f:
      passwords = f.read().split("\n") # Datei wird eingelesen und am Zeilenumbruch geteilt
  ```

  Nach dem Import und dem Einlesen muss eine Funktion definiert werden, die die Zip-Datei entpackt.
  Diese Funktion...
  1. bekommt als Parameter den Dateinamen der aktuellen Zip-Datei übergeben,
  2. (optional) prüft, ob es sich bei der Datei um eine Zip-Bombe handelt,
  3. entpackt die Zip-Datei
     1. Bei einem RuntimeError wird die Passwortliste verwendet
     2. Es werden alle Passwörter aus der rockyou.txt mit einer Länge von 96 Zeichen Ausprobiert
     3. Bei Erfolg wird das Passwort ausgegeben
  4. löscht die alte Datei.

  Im Code sieht das dann so aus:
  ```python3
  def extract(filename):
      path = "extracted/" + filename
      if not (detect_zip_bomb.pruefen(path) == False): # optional
          raise Exception # optional
      z = zipfile.ZipFile(path) # öffnet die Zip-Datei und speichert dies in der Variable z
      try:
          z.extractall("extracted") # entpackt die Datei in den Ordner extracted/
      except RuntimeError: # Fehler wird geworfen, wenn die Zip-Datei ein Passwort verlangt
          for pw in passwords: # für jedes Passwort in der Passwort-Liste
              if len(pw) >= 96:  # durch den Hinweis wissen wir, dass das Passwort 96 Zeichen lang ist. Bei unbekannter Länge kann dieses if statement auch entfernt werden
                  try:
                      z.extractall("extracted", pwd=str.encode(pw)) # Datei wird mit dem Passwort in den Ordner extracted/ extrahiert
                      print({"file": z, "password": pw, "filename": filename}) # bei Erfolg wird Ausgegeben, welche Zip-Datei mit welchem Passwort verschlüsselt wird
                      break # stopp nach Erfolg
                  except RuntimeError: # Fehler wird geworfen, wenn das Passwort falsch ist
                      pass # nichts machen
      except FileNotFoundError:
          print(FileNotFoundError) # bei einem FileNotFoundError stoppt das Script nicht, sondern macht mit den anderen Zip-Dateien weiter
      os.remove(path)
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

# Frohe Weihnachten 

Danke, dass ihr euch die Zeit genommen habt, euch dieses Repository anzuschauen.

Ich wünsche alles Gute, bleibt gesund und genießt die Feiertage!