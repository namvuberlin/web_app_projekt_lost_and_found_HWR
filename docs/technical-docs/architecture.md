---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Lost & Found Web App]

{: .no_toc }
# Architecture

{: .attention }
> This page describes how the application is structured and how important parts of the app work.
> It should give a new contributor sufficient technical knowledge for contributing to the codebase.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

---

## Overview

Die **Lost & Found Web App** ist eine Webanwendung für Hochschulen, mit der Studierende verlorene oder gefundene Gegenstände melden können.  
Neben Studierenden existiert eine **Admin-Rolle** (z. B. Hausmeister oder Fundstellenmitarbeiter), die Beiträge verwaltet und globale Einstellungen pflegt.

Zentrale Funktionen:
- Authentifizierung über Benutzername und Passwort
- Zwei Rollen: Student und Admin
- Erstellen, Bearbeiten und Löschen von Lost- und Found-Beiträgen
- Detailansichten mit Erstellerinformationen
- Mitteilungsfunktion für Interessenten
- Administrationsbereich mit Statistik-Dashboard und Einstellungen

Die Anwendung basiert auf **Flask** für Routing und Request-Handling, **Jinja2** für serverseitiges Rendering, **SQLAlchemy** als ORM und **SQLite** als Datenbank.

---

## Codemap

Die Anwendung folgt einer bewusst einfachen Flask-Struktur, um Wartbarkeit und Verständlichkeit zu gewährleisten.

### `app.py`

Zentrale Steuerung der Anwendung:
- Initialisierung der Flask-App und Konfiguration
- Definition aller Routen für Authentifizierung, Student- und Admin-Bereich
- Verwaltung von Sessions (`user_id`, `is_admin`)
- Zugriffskontrolle über Decorators (`login_required`, `admin_required`)
- Initialisierung der Datenbank und Erstellen eines festen Admin-Benutzers

### `db.py`

Enthält das komplette Datenbankmodell mittels SQLAlchemy:
- **User**: Benutzerkonten mit Rolle, Matrikelnummer und E-Mail
- **ItemPost**: Lost- und Found-Beiträge inkl. Status und Ersteller
- **PostInterest**: Mitteilungen von Nutzern zu Beiträgen
- **AppSettings**: Globale Anwendungseinstellungen (Station, Kontakt)

Die Beziehungen zwischen den Tabellen werden über Foreign Keys und ORM-Beziehungen abgebildet.

### `templates/`

Alle Benutzeroberflächen werden serverseitig mit Jinja2 gerendert:
- `base.html`: Zentrales Layout und Navigation
- `auth/`: Login- und Registrierungsseiten
- `student/`: Dashboard, Listen, Detailansichten, Profile, Mitteilungen
- `admin/`: Dashboard, Beitragsverwaltung, Benutzerverwaltung, Settings


