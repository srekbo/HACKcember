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

Falls ich demnächst Zeit und Lust dazu habe, werde ich noch Kommentare einfügen, damit die einzelnen Schritte besser verständlich sind.

# Frohe Weihnachten 

Danke, dass ihr euch die Zeit genommen habt, euch dieses Repository anzuschauen.

Ich wünsche alles Gute, bleibt gesund und genießt die Feiertage!