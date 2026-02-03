---
title: Design Decisions
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Rollenbasierte Zugriffe (Student / Admin)

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

In einer Lost-&-Found-App sind bestimmte Aktionen sensibel (z. B. Posts löschen).  
Wenn jede*r alles ändern/löschen kann, sinkt die Sichherheit und es entstehen Missbrauchsversuche.


### Decision

Wir unterscheiden zwei Rollen:

- **Student**: kann Posts erstellen und eigene Posts verwalten (z. B. Status ändern / bearbeiten).
- **Admin (Pförtner)**: kann Posts moderieren und bei Bedarf löschen/abschließen.

### Regarded options

+ **Keine Rollen** (alle dürfen alles) - Missbrauch
+ **Zwei Rollen** (Student/Admin) - unterschiedliche Zugriffsrechte

---

## 02: Bootstrap

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

Wir benötigen ein responsives UI (Buttons, Forms, Cards, Navigation), ohne viel eigenes CSS zu schreiben und ohne zusätzliche Frontend-Frameworks.

### Decision

Wir verwenden Bootstrap als UI-Framework, statt eigenes CSS zu schreiben oder uns in Tailwind CSS einzuarbeiten.

Begründung:
- Schnelle und einfache Umsetzung eines konsistenten Layouts
- Responsives Design
- Gute Unterstützung für Formulare und Standard-Komponenten

### Regarded options

| Kriterium | Bootstrap 5 (gewählt) | Eigenes CSS | Tailwind CSS |
| --- | --- | --- | --- |
| **Einarbeitung** | ✔️ schnell (viele fertige Klassen) | ❌ dauert (alles selbst definieren) | ❔ extra Konzept (Utility-Ansatz) |
| **Tempo beim Umsetzen** | ✔️ sehr schnell | ❌ eher langsam | ✔️ schnell, wenn man es kann |
| **Responsive Layout** | ✔️ direkt enthalten | ❌ muss man selbst bauen | ✔️ vorhanden |
| **Komponenten** (Buttons, Forms, Nav) | ✔️ viele sofort nutzbar | ❌ alles selbst bauen | ❌ selbst zusammenbauen |
| **Passend zur Kursabgabe** | ✔️ unkompliziert | ✔️ möglich, aber mehr Aufwand | ❔ zusätzlicher Lernaufwand |

---

## 03: Getrennte Views für Missing & Found Items

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

User suchen entweder verlorene Gegenstände oder melden gefundene Gegenstände.  
Wenn alles in einer Liste vermischt ist, wird die Orientierung schlechter und Filterung/Navigation wird unklar.

### Decision

Wir trennen die Darstellung in zwei eigene Seiten:

- **Missing Items**: Liste für verlorene Gegenstände
- **Found Items**: Liste für gefundene Gegenstände

Vorteil: klare Nutzerführung, weniger Verwirrung.

### Regarded options

| Criterion | Eine Seite (gemischt) | Zwei Seiten (gewählt) |
| --- | --- | --- |
| **Schnell ans Ziel** | ❌ erst suchen/scrollen | ✔️ direkt richtige Liste |
| **Orientierung** | ❌ unübersichtlicher | ✔️ klare Trennung |
| **Umsetzung** | ✔️ einfach | ✔️ einfach |

---

## 04: base.html (Template Layout)

### Meta

Status
: **Work in progress** - Decided - Obsolete

Updated
: DD-MMM-YYYY

### Problem statement

Viele Seiten teilen sich UI-Bausteine wie:
- Navigation / Header
- Footer
- Einbindung von Bootstrap/CSS
- Flash-Messages

Wenn jede Seite das mehrfach enthält, entsteht Duplicate Code und Inkonsistenz bei Änderungen.

### Decision

Wir nutzen eine zentrale **`base.html`** als Layout-Template und lassen andere Templates davon **erben** (Jinja2 `extends` + `block`).

Vorteile:
- Änderungen am Layout nur an einer Stelle
- Einheitliches UI über alle Seiten

### Regarded options

| Criterion | Copy/Paste Layout | base.html (gewählt) |
| --- | --- | --- |
| Wartbarkeit | ❌ | ✔️ |
| Konsistenz | ❌ | ✔️ |
| Aufwand initial | ✔️ | ✔️ |
