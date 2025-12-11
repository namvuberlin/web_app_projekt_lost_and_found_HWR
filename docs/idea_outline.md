# Lost & Found HWR — Idea Outline

## Team Information

*Team Name:*
Lost & Found HWR

*Contributors:*
Nam Tung Vu, Suheib Abdolkadir Mohammed Saaid


*Repository Link:*
https://github.com/namvuberlin/web_app_projekt_lost_and_found_HWR

---

## Value Proposition

### Problem
An der HWR Berlin gehen regelmäßig persönliche Gegenstände verloren (Studentenausweise, Schlüssel, Ladegeräte, Kleidung usw.).
Der aktuelle Prozess ist kompliziert und unübersichtlich:

- Gefundene Gegenstände werden bei den Pförtnern in Haus A, B oder E abgegeben.
- Studierende müssen mehrere Standorte ablaufen, um nachzufragen.
- Alternativ werden WhatsApp-Gruppen genutzt – diese erreichen aber *nicht alle* und Informationen gehen schnell verloren.

### Lösung
Lost & Found HWR ist eine digitale Anzeigetafel für Studierende der HWR Berlin.
Sowohl Finder als auch *Suchende* können sich anmelden und Posts erstellen.

Funktionen:
- Beiträge mit Titel, Beschreibung, Standort, Foto und Kontaktdaten erstellen.
- Alle Posts erscheinen auf einer gemeinsamen Pinnwand.
- Kommunikation und Übergabe erfolgen direkt zwischen den Studierenden 
  die Plattform selbst *nimmt keine Vermittlerrolle ein*.
- Dadurch bleibt das System einfach, datenschutzfreundlich und leicht nutzbar.

### Zielgruppe
- Studierende der HWR Berlin
- Optional: Mitarbeitende (z. B. Pförtner), die Fundmeldungen einsehen möchten

---

## Tentative UI Screens

**1. Login & Register Screens**
* **Login:** Eine einfache Seite zur Eingabe von `username` und `password` mit "Login"-Button.
* **Register:** Eine separate Seite zur Erstellung eines neuen Kontos, ebenfalls mit `username` und `password`.

**2. Student Dashboard (Die Hauptansicht für Nutzer)**
* Dies ist die "Pinnwand" nach dem Login für Studierende.
* Zeigt eine persönliche Übersicht mit Tabs für:
    * **Meine Posts:** Eine Liste der eigenen erstellten Beiträge (z.B. "Armbanduhr", "Aasas Laptop").
    * **Neue Nachrichten:** (Impliziert ein Nachrichtensystem).
    * **Neue Fundmeldungen:** (Impliziert Benachrichtigungen).
* Die Post-Liste zeigt Details wie Titel, Student, Typ, Standort, Status und Datum.
* Es gibt Buttons zur Verwaltung: `+ Neuer Post erstellen`, `Post bearbeiten` und `Post löschen`.

**3. Admin Dashboard (Eigener Bereich für Verwaltung)**
* Eine separate Ansicht für Admins (nicht für normale Studierende sichtbar).
* Zeigt eine Statistik (z.B. "Posts in total").
* Bietet Verwaltungsfunktionen für `Posts` und `Users` (Nutzer).
* Admins können hier Posts auflisten, bearbeiten oder neue hinzufügen (laut Notiz).

**4. Neuer Post erstellen (Impliziert durch Button)**
* Eine Seite oder ein Formular (noch nicht gezeichnet), das sich öffnet, wenn der Nutzer auf `+ Neuer Post erstellen` klickt.
* Enthält Felder für Titel, Beschreibung, Standort, Bild-Upload, Typ (Gefunden/Gesucht) und Kontaktinfos.

**5. Post Detail Page (Impliziert durch Notiz)**
* Die "Ansicht der Artikel" (noch nicht gezeichnet).
* Öffnet sich, wenn man auf einen Post in der Liste klickt und zeigt alle Details (großes Bild, Beschreibung etc.).

**Unsere ersten Entwürfe und Scribbles haben wir auf Miro festgehalten**

**[Hier klicken, um unser Miro Board mit den UI-Entwürfen zu öffnen](https://miro.com/welcomeonboard/bkFKRnNSdDhoc3JMSjBWTXR1TWNZNUVNUXJTaUs0UXFEN2IxVitxOUsrZVpjdnY5M0dwcWhYWm5RV3d6aC9nTVNmNkFpdDRKZ1pJMEtQWHM0UkFhd2FPQ2xXQk90YUZ4dmhabEltZGFpbUlOUVVWYTBzY3BxcStoM2RZT0MzVW53VHhHVHd5UWtSM1BidUtUYmxycDRnPT0hdjE=?share_link_id=322240114000)**

---

## Nutzungskonzept & Entscheidungslogik

### Konzept: Digitale Anzeigetafel
Die Plattform dient als neutrales Schwarzes Brett:
- Nutzer posten eigenverantwortlich (kein Moderator nötig).
- Finder und Suchende kommunizieren direkt untereinander.
- Die Plattform hält sich aus Rückgabeentscheidungen heraus.

### Umgang mit Konflikten
Wenn mehrere Personen denselben Gegenstand beanspruchen:
- Fokus auf Kontaktdaten:
- Anbieten von direkten Kontaktmöglichkeiten: Anzeigen einer E-Mail-Adresse oder Telefonnummer (mit Einverständnis).
- Empfehlung für Beweisfragen:
- Hinweis in der App: Text einblenden (z.B. im FAQ): "Wenn sich mehrere Personen melden, fragen Sie nach spezifischen Merkmalen des Gegenstands, die nur der wahre Besitzer kennen kann".

---

## Team Goals

*Gruppenziel:*
- Funktionierende Web-App mit:
  - Registrierung/Login
  - Posts mit Bild-Upload
  - Öffentlicher Pinnwand
  - Einfacher Suche/Filterfunktion

*Individuelle Ziele:*
- *Suheib:* Frontend, UI-Komponenten
- *Nam:* Backend, Datenbankstruktur und Authentifizierung

---

## Erweiterungsideen (Future Features)

- Pförtner-Accounts mit Admin-Rechten (z. B. Posts prüfen oder löschen)
- Markierung: „Gefunden“, „Abgeholt“ oder „Offen“
