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

Wir nutzen Bootstrap als UI-Framework.

Begründung:
- Schnelle Umsetzung eines konsistenten Layouts
- Responsives Design
- Gute Unterstützung für Formulare und Standard-Komponenten

### Regarded options

| Criterion | Eigenes CSS | Bootstrap (gewählt) |
| --- | --- | --- |
| **Entwicklungszeit** | ❌ langsam (viel selbst bauen) | ✔️ schnell (fertige Komponenten) |
| **Konsistenz** | ❌ oft uneinheitlich | ✔️ einheitlicher Look |
| **Responsive Design** | ❌ extra Aufwand | ✔️ eingebaut (Grid/Breakpoints) |
| **Wartbarkeit** | ❌ mehr eigener Code | ✔️ weniger eigener CSS-Code |

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

Wir haben zwei Möglichkeiten betrachtet:

+ **Eine gemeinsame Seite** (Missing & Found zusammen)
+ **Zwei getrennte Seiten** (Missing-Seite und Found-Seite) ✅

| Criterion | Eine Seite (gemischt) | Zwei Seiten (gewählt) |
| --- | --- | --- |
| **Schnell ans Ziel** | ❌ erst suchen/scrollen | ✔️ direkt richtige Liste |
| **Orientierung** | ❌ unübersichtlicher | ✔️ klare Trennung |
| **Umsetzung** | ✔️ einfach | ✔️ einfach |

