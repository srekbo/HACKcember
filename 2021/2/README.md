# Challenge 2: Die GEMÄLDE von R. Udolf und S. Klaus

Zum Video geht es [hier](https://youtu.be/kM_DMMb6hgs) und zur Erklärung auf der Website [hier](https://www.floriandalwigk.de/die-gem%C3%A4lde-von-r-udolf-und-s-klaus/).

## Beschreibung (von der Website)

Heute geht es um abstrakte Weihnachtskunst. Genauer gesagt um diese beiden Gemälde hier:

### "Weihnachtsschlange" - R. Udolf
![](https://image.jimcdn.com/app/cms/image/transf/dimension=890x10000:format=png/path/s6cc09bec31deaeb6/image/i4d0c27157453ca78/version/1638455998/image.png)

### "Weihnachts-Algorithmus" - S. Klaus
![](https://image.jimcdn.com/app/cms/image/transf/dimension=890x10000:format=png/path/s6cc09bec31deaeb6/image/i4ef87d39aaee2e4e/version/1638456028/image.png)

Sind sie nicht schön? Das erste Bild stammt von dem berühmten Künstler R. Udolf und das zweite von S. Klaus. Beide hängen auf eine mysteriöse Art zusammen und bergen ein Geheimnis. ENTWEDER bringst du diese beiden Bilder irgendwie zusammen ODER du wirst das Geheimnis niemals lüften.
<br>Finde das Passwort und schalte damit das nächste Hacking-Video frei.
<br>Ich wünsche dir viel Erfolg!

## Was ist zu tun?

Die beiden Bilder müssen verXORt werden.

## Lösung

Die Lösung ist in der Datei "main.py".

<details>
  <summary>Für die Erklärung hier klicken</summary>

  Für das Script brauchen wir von dem Modul PIL zwei Module:
  1. Image - öffnen der Bilder
  2. ImageChops.logical_xor() - XOR der beiden Bilder
  
  Als Erstes muss das Modul importiert werden:
  ```python3
  from PIL import Image, ImageChops
  ```
  Fertig!

  Jetzt kann das Script geschrieben werden:
  ```python3
  if __name__ == "__main__":
      image1 = Image.open("image.png").convert("1") # 1. Bild S/W einlesen
      image2 = Image.open("image2.png").convert("1") # 2. Bild S/W einlesen
      r = ImageChops.logical_xor(image1, image2) # 1. und 2. Bild verXORen
      r.save("res.png") # Ergebnis wird als res.png gespeichert
  ```
  Viel Spaß beim Ausprobieren!
</details>

