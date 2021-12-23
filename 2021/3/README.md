# Challenge 3: Das CYBER-ROTKÄPPCHEN

Zum Video geht es [hier](https://youtu.be/pfivHCLHIus) und zur Erklärung auf der Website [hier](https://www.floriandalwigk.de/das-cyber-rotkaeppchen).

Der Märchen-Text ist in der Datei cyber-rotkaeppchen.md gespeichert.

## Beschreibung (von der Website)

Dies ist ein Märchen. Ein Cyber-Märchen. Wie 1 und 0 cyberts in diesem Märchen, mal mit und mal ohne Bindestrich. Mehr möchte ich dir als Tipp an dieser Stelle nicht mitgeben.
* Das ursprüngliche Märchen stammt von grimmstories.com. 

## Was ist zu tun?

Bei jedem "cyber-" muss einem String eine 1 und bei jedem "cyber" eine 0 angefügt werden.

Am Ende muss der Binary-Code in ASCII umgewandelt werden.

## Lösung

Die Lösung ist in der Datei "main.py".

<details>
  <summary>Für die Erklärung hier klicken</summary>

  Der erste Schritt ist das Einlesen des Märchen:

  ```python3
  with open("cyber-rotkaeppchen.md") as f:
      text = f.read()
  ```

  Danach muss der Hauptteil gemacht werden:
  ```python3
  binary = "" # Variable, in der der Binärcode gespeichert wird
  for word in text.split(" "): # für jedes Wort in dem Text (an einem Leerzeichen getrennt)
      if "cyber" in word.lower(): # wenn in dem Wort "cyber" ist
          if "cyber-" in word.lower(): # wenn in dem Wort "cyber-" ist
              binary += "1" # dem String eine 1 am Ende hinzufügen
          else: # wenn kein "-" hinter dem Cyber ist
              binary += "0" # dem String eine 0 am Ende hinzufügen
  ```
  Jetzt nur noch die Binärdaten in ASCII umwandeln (da hat Stackoverflow mir geholfen xD) und ausgeben:
  ```python3
  ascii_code = ''.join(chr(int(binary[i * 8:i * 8 + 8], 2)) for i in range(len(binary) // 8))
  print("Binary:\n"+binary)
  print("Entschlüsseltes PW:\n"+ascii_code)
  ```
  Viel Spaß beim Ausprobieren!
</details>