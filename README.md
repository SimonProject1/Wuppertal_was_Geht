# Wuppertal, was geht? V0.3.0

## Neu
- vereinfachter 3-Fragen-Assistent
- Bereich „Heute in Wuppertal“
- Filter Heute, Morgen, Wochenende und Kategorien
- Eventdaten mit Quelle, Status und Prüfzeit
- Favoriten und responsive PWA

## Datenaktualisierung
`data/events.json` enthält die kontrollierten Eventdaten. Die mitgelieferte GitHub Action prüft täglich, ob die Datei syntaktisch gültig und nicht veraltet ist. Eine automatische Übernahme aus dem offiziellen Veranstaltungskalender setzt eine freigegebene API/Feed-Nutzung oder eine separate rechtlich und technisch geprüfte Importanbindung voraus. Bis dahin Events nur aus offiziellen Quellen eintragen.

## Veröffentlichung
Alle Dateien in ein GitHub-Repository laden und GitHub Pages aus `main / root` aktivieren.
