# raetselbox
FProg Projekt

## TODO
- [ ] Rätsel schreiben
  - [ ] Sumpf
  - [ ] Arktik
  - [ ] Pyramide
  - [ ] Atlantis
  - [ ] Master-Rätsel?  
    müssen eventuell nur den Code prüfen
- [ ] Treiber programmieren
- [ ] Rätsel-loop schreiben
  - [ ] Rätsel aus JSON einlesen
  - [ ] Rätsel initialisieren (Rätsel-Klasse?)
  - [ ] Rätsel stellen
  - [ ] Hinweise(? - eventuell optional)
  - [ ] Lösung prüfen (nur Sensoren?)
- [ ] Konfiguration (Python)
  - [ ] Benutzer nach Eingaben für Text, Werte etc. fragen
  - [ ] JSON nach Angaben des Nutzers schreiben
  - [ ] JSON so konfigurieren, dass sie in der main verlinkt werden  
    Im Moment haben wir ja die 4 Szenarien fest kodiert. Eventuell können wir die festen Dateien durch Platzhalter ersetzen wie `scenario1.json` und `scenario2.json`. In `scenario1.json` gibt es dann einen Verweis auf die tatsächliche JSON-Datei, die gelesen werden soll. So müssen wir nicht den Code an sich ändern, sondern bei der Konfiguration nur den Dateinamen in die JSON-Dateien schreiben.
