---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

{: .attention }
> This page collects internal functions, routes with their functions, and APIs (if any).
> 
> See [Uber](https://developer.uber.com/docs/drivers/references/api) or [PayPal](https://developer.paypal.com/api/rest/) for exemplary high-quality API reference documentation.
>
> You may delete this `attention` box.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## [Section / module]

### `function_definition()`

**Route:** `/route/`

**Methods:** `POST` `GET` `PATCH` `PUT` `DELETE`

**Purpose:** [Short explanation of what the function does and why]

**Sample output:**

[Show an image, string output, or similar illustration -- or write NONE if function generates no output]

---

## Authentication

### `login()`

**Route:** `/login`

**Methods:** `GET`, `POST`

**Purpose:**  
Authentifiziert einen Student- oder Admin-Benutzer anhand von Benutzername und Passwort.

**Database interaction:**  
- READ `users`

**Sample output:**  
Login-Formular oder Weiterleitung zum Dashboard

---

### `register()`

**Route:** `/register`

**Methods:** `GET`, `POST`

**Purpose:**  
Registriert einen neuen Student-Benutzer und speichert die Zugangsdaten sicher in der Datenbank.

**Database interaction:**  
- READ `users`  
- WRITE `users`

**Sample output:**  
Registrierungsformular oder erfolgreiche Weiterleitung

---

## Student functionality

### `student_dashboard()`

**Route:** `/dashboard`

**Methods:** `GET`

**Purpose:**  
Zeigt das Student-Dashboard mit einer Übersicht über eigene Beiträge und aktuelle Einträge.

**Database interaction:**  
- READ `items`  
- READ `claims`

**Sample output:**  
Student-Dashboard-Ansicht

---

### `list_items()`

**Route:** `/items`

**Methods:** `GET`

**Purpose:**  
Listet alle gemeldeten verlorenen und gefundenen Gegenstände auf.

**Database interaction:**  
- READ `items`

**Sample output:**  
Liste der Lost- und Found-Items

---

### `create_item()`

**Route:** `/items/create`

**Methods:** `GET`, `POST`

**Purpose:**  
Ermöglicht es einem Studenten, einen neuen Verlust- oder Fundbeitrag zu erstellen.

**Database interaction:**  
- WRITE `items`

**Sample output:**  
Formular zur Item-Erstellung oder Bestätigung

---

### `claim_item(item_id)`

**Route:** `/items/<int:item_id>/claim`

**Methods:** `POST`

**Purpose:**  
Ermöglicht es einem Studenten, einen Anspruch auf einen Gegenstand zu stellen.

**Database interaction:**  
- WRITE `claims`

**Sample output:**  
Anspruch wurde eingereicht (Status: pending)

---

## Admin functionality

### `admin_dashboard()`

**Route:** `/admin/dashboard`

**Methods:** `GET`

**Purpose:**  
Zeigt eine administrative Übersicht über Beiträge, offene Ansprüche und Benutzer.

**Database interaction:**  
- READ `items`  
- READ `claims`  
- READ `users`

**Sample output:**  
Admin-Dashboard-Ansicht

---

### `review_claim(claim_id)`

**Route:** `/admin/claims/<int:claim_id>`

**Methods:** `POST`

**Purpose:**  
Ermöglicht es einem Administrator, einen Anspruch zu genehmigen oder abzulehnen.

**Database interaction:**  
- WRITE `claims`  
- WRITE `items`

**Sample output:**  
Anspruch wurde genehmigt oder abgelehnt

