# AI-Code-Monitor (Lama)
Ein Python-basiertes Automatisierungstool zur Echtzeit-Analyse von Quellcode unter Verwendung lokaler Sprachmodelle (LLMs).

# Beschreibung
Dieses Tool überwacht eine spezifische Python-Datei auf Änderungen. Sobald die Datei gespeichert wird, extrahiert das Skript den Inhalt und sendet ihn an eine lokale Instanz von Ollama (Llama3). Die KI fungiert als "virtueller Mentor", der den Code auf Syntaxfehler prüft, logische Korrekturen vorschlägt oder auf spezifische Fragen in den Kommentaren antwortet.
Das Projekt demonstriert die Integration von lokaler KI in den Entwicklungsprozess zur Steigerung der Effizienz und Fehlervermeidung.

# Kernfunktionen
Automatisierte Überwachung: Erkennt Dateispeicherungen (File-Watch-Logik) in Echtzeit.
KI-Integration: Schnittstelle zur ollama Bibliothek für lokale, datenschutzkonforme Code-Analyse.
Interaktives Feedback: Ausgabe von Fehlermeldungen, Korrekturvorschlägen oder Erklärungen direkt im Terminal.
Syntax-Check & Mentoring: Erkennt Fehler und beantwortet im Code gestellte Fragen (z. B. # wie mache ich...).
Technische Anforderungen
Python 3.x
Ollama mit installiertem llama3 Modell
Python-Bibliothek ollama (pip install ollama)
Installation & Start
Repository klonen oder Skript kopieren.
Sicherstellen, dass Ollama im Hintergrund läuft.
Die zu prüfende Datei (z. B. check_me.py) erstellen.
