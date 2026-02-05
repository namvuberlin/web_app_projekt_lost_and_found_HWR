---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Lost & Found Web App]

{: .no_toc }
# Reference documentation

{: .attention }
> This page collects internal routes, their functions, and database interactions
> of the Lost & Found web application.
> The application is implemented using Flask, Jinja2, SQLAlchemy, and SQLite.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

---

## Authentication

### `login()`

**Route:** `/login`  
**Methods:** `GET`, `POST`

**Purpose:**  
Authentifiziert einen Student-Benutzer anhand von Benutzername und Passwort.

**Database interaction:**  
- READ `users`

**Sample output:**  
Login form or redirect to student dashboard

---

### `admin_login()`

**Route:** `/admin/login`  
**Methods:** `GET`, `POST`

**Purpose:**  
Authentifiziert einen Administrator-Benutzer.

**Database interaction:**  
- READ `users`

**Sample output:**  
Admin login form or redirect to admin dashboard

---

### `register()`

**Route:** `/register`  
**Methods:** `GET`, `POST`

**Purpose:**  
Registriert einen neuen Student-Benutzer inklusive Matrikelnummer und Hochschul-E-Mail.

**Database interaction:**  
- READ `users`  
- WRITE `users`

**Sample output:**  
Registration form or redirect to login page

---

### `logout()`

**Route:** `/logout`  
**Methods:** `GET`

**Purpose:**  
Beendet die aktuelle Sitzung durch Löschen der Session.

**Database interaction:**  
- NONE

**Sample output:**  
Redirect to login page

---

## Student functionality

### `student_dashboard()`

**Route:** `/student/dashboard`  
**Methods:** `GET`

**Purpose:**  
Zeigt eine Übersicht über:
- eigene Beiträge
- offene Beiträge
- Mitteilungen der aktuellen Woche
- zuletzt erstellte Beiträge

**Database interaction:**  
- READ `item_posts`  
- READ `post_interests`

**Sample output:**  
Student dashboard view

---

### `student_lost()`

**Route:** `/student/lost`  
**Methods:** `GET`

**Purpose:**  
Listet alle als verloren gemeldeten Gegenstände auf.

**Database interaction:**  
- READ `item_posts`

**Sample output:**  
Table view of lost items

---

### `student_found()`

**Route:** `/student/found`  
**Methods:** `GET`

**Purpose:**  
Listet alle als gefunden gemeldeten Gegenstände auf.

**Database interaction:**  
- READ `item_posts`

**Sample output:**  
Table view of found items

---

### `student_new_post()`

**Route:** `/student/post/new`  
**Methods:** `GET`, `POST`

**Purpose:**  
Erstellt einen neuen Fund- oder Verlustbeitrag.

**Database interaction:**  
- WRITE `item_posts`

**Sample output:**  
Post creation form

---

### `student_post_detail(post_id)`

**Route:** `/student/post/<int:post_id>`  
**Methods:** `GET`

**Purpose:**  
Zeigt eine Detailansicht eines Beitrags inklusive Erstellerdaten
und eingegangener Mitteilungen.

**Database interaction:**  
- READ `item_posts`  
- READ `users`  
- READ `post_interests`

**Sample output:**  
Item detail view

---

### `student_post_respond(post_id)`

**Route:** `/student/post/<int:post_id>/respond`  
**Methods:** `POST`

**Purpose:**  
Ermöglicht es einem Benutzer, sich auf einen Gegenstand zu melden
und eine Nachricht zu hinterlassen.

**Database interaction:**  
- WRITE `post_interests`

**Sample output:**  
Redirect to item detail view

---

### `student_edit_post(post_id)`

**Route:** `/student/post/<int:post_id>/edit`  
**Methods:** `GET`, `POST`

**Purpose:**  
Bearbeitet einen eigenen Beitrag (Titel, Beschreibung, Ort, Status).

**Database interaction:**  
- READ `item_posts`  
- WRITE `item_posts`

**Sample output:**  
Edit form or redirect to dashboard

---

### `student_delete_post(post_id)`

**Route:** `/student/post/<int:post_id>/delete`  
**Methods:** `POST`

**Purpose:**  
Löscht einen eigenen Beitrag.

**Database interaction:**  
- DELETE `item_posts`

**Sample output:**  
Redirect to student dashboard

---

### `student_messages()`

**Route:** `/student/messages`  
**Methods:** `GET`

**Purpose:**  
Zeigt alle Mitteilungen an, die andere Benutzer zu den eigenen Beiträgen
gesendet haben.

**Database interaction:**  
- READ `post_interests`  
- READ `users`

**Sample output:**  
Messages overview

---

### `student_profile()`

**Route:** `/student/profile`  
**Methods:** `GET`

**Purpose:**  
Zeigt alle Profildaten des angemeldeten Studenten.

**Database interaction:**  
- READ `users`  
- READ `app_settings`

**Sample output:**  
Student profile view

---

## Admin functionality

### `admin_dashboard()`

**Route:** `/admin/dashboard`  
**Methods:** `GET`

**Purpose:**  
Zeigt eine administrative Gesamtübersicht über Beiträge und Benutzer.

**Database interaction:**  
- READ `item_posts`  
- READ `users`

**Sample output:**  
Admin dashboard view

---

### `admin_posts()`

**Route:** `/admin/posts`  
**Methods:** `GET`

**Purpose:**  
Listet alle Beiträge mit Filter- und Suchfunktionen.

**Database interaction:**  
- READ `item_posts`

**Sample output:**  
Admin post list

---

### `admin_posts_new()`

**Route:** `/admin/posts/new`  
**Methods:** `GET`, `POST`

**Purpose:**  
Erstellt einen neuen Beitrag als Administrator.

**Database interaction:**  
- WRITE `item_posts`

**Sample output:**  
Admin post creation form

---

### `admin_posts_edit(post_id)`

**Route:** `/admin/posts/<int:post_id>/edit`  
**Methods:** `GET`, `POST`

**Purpose:**  
Bearbeitet bestehende Beiträge unabhängig vom Ersteller.

**Database interaction:**  
- READ `item_posts`  
- WRITE `item_posts`

**Sample output:**  
Admin edit form

---

### `admin_posts_delete(post_id)`

**Route:** `/admin/posts/<int:post_id>/delete`  
**Methods:** `POST`

**Purpose:**  
Löscht einen Beitrag aus dem System.

**Database interaction:**  
- DELETE `item_posts`

**Sample output:**  
Redirect to admin post list

---

### `admin_users()`

**Route:** `/admin/users`  
**Methods:** `GET`

**Purpose:**  
Listet alle registrierten Benutzer.

**Database interaction:**  
- READ `users`

**Sample output:**  
User management table

---

### `admin_user_delete(user_id)`

**Route:** `/admin/users/<int:user_id>/delete`  
**Methods:** `POST`

**Purpose:**  
Löscht einen Student-Benutzer aus dem System.
Administratoren können nicht gelöscht werden.

**Database interaction:**  
- DELETE `users`

**Sample output:**  
Redirect to user list

---

### `admin_settings()`

**Route:** `/admin/settings`  
**Methods:** `GET`, `POST`

**Purpose:**  
Verwaltet globale Anwendungseinstellungen wie Stationsname
und Kontakt-E-Mail-Adresse.

**Database interaction:**  
- READ `app_settings`  
- WRITE `app_settings`

**Sample output:**  
Settings form
