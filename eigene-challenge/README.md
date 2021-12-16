# Eigene Challenge

Hi, hier ist meine Challenge für alle, die sich dieses Repo anschauen!

## Beschreibung

Diese Challenge hat zwei Teile.

Der erste Teil orientiert sich an der 1. HACKcember challenge. Hier sind zwei Dateien knapp über 100x verpackt!
<br>Das Problem: Vor dem Geschenkpapier ist manchmal ein Schloss! Da dies eine CTF-Challenge ist, empfehle ich eine Passwortliste, die für CTF oft genutzt wird.

Der zweite Teil ist geheim.
Tips gibt es unter dem dritten Punkt [Lösungen](README.md#lsung)

Auf einem Debian 10 Server dauert das Script für Teil 1 ca. 20 Minuten (in meinem Script wurde auch ein detector für zip-bomben eingebaut).
Auf einem raspi mit 8 s pro tausend extractionsversuchen dauert es ca 2 h.
## Hinweise

<details>
  <summary>Spoiler warning - Hinweis zur Passwortdatei</summary>
  Eine beliebte Passwort-Datei für CTF-Challenges ist rockyou.txt<br>
  Aus dieser Datei wurden zufällige Passwörter ausgewählt.
</details>
<br>
<details>
  <summary>Spoiler warning - Hinweis zum 2. Teil</summary>
  xor
</details>
<br>
<details>
  <summary>Spoiler warning - 2. Hinweis zum 2. Teil</summary>
  One Time Pad
</details>

## Lösung

<details>
  <summary>Spoiler warning - Lösung des Teil 1</summary>

  Als Erstes musst du das Geschenkpapier entfernen.
  Leider ist am Geschenkpapier manchmal ein Schloss.
  Was bedeutet das?
  Du musst ein Script schreiben, dass
  1. das Geschenkpapier entfernt und
  2. immer wenn ein Schloss vor dem Geschenkpapier ist, dieses knackt.

  Als Erstes müssen Pakete importiert werden:
  * os: Löschen der entpackten Dateien und Inhalte eines Ordners Auflisten 
  * zipfile: Entpacken der Dateien
  ~~~python3
  import os
  import zipfile
  ~~~
  Als Nächstes muss eine Passwort-Datei (ich nehme Teile der rockyou.txt) eingelesen und eine eine Funktion definiert werden, die
  1. die Datei entpackt,
  2. eine Dictionary-Attacke macht und
  3. die alte Datei löscht.
  Wir nennen diese Funktion extract()
  ~~~python3
  with open("rockyou-short.txt") as f:
      passwords = f.read().split("\n")

  def extract(filename):
      filename = "extracted/" + filename # Zip-Datei wird in extracted/ abgelegt
      z = zipfile.ZipFile(filename)
      try:
          z.extractall()
      except RuntimeError: # Error, der durch ein falsches Passwort ausgelöst wird
          for pw in passwords:
              try:
                  z.extractall(pwd=str.encode(pw))
                  break #wenn das script bis hier gekommen ist, stoppt es die for-Schleife
              except RuntimeError:
                  pass
      os.remove(filename) # löscht die ursprüngliche Datei
  ~~~
  Fast geschafft: jetzt muss diese Funktion nur noch aufgerufen werden
  ~~~python3
  if __name__ == "__main__":
      while True:
          dirlist = os.listdir("extracted") # speichert alle Dateien in extracted/ in ein Array
          zipcounter = 0 # zähler für Zip-Dateien
          for file in dirlist:
              if file.endswith(".zip"):
                  extract(file)
                  zipcounter += 1
          if zipcounter == 0:
              break
  ~~~
  
</details>
<br>
<details>
  <summary>Spoiler warning - Lösung zum 2. Teil</summary>
  Eine Erklärung zu diesem Teil kommt demnächst.

  Falls ihr auch mit den beiden Hinweisen nicht weiterkommt, tut ihr das hoffentlich nach <a href="https://youtu.be/RowdpaEQPUA">diesem Video</a>!
</details>
