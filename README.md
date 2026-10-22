# TA App — Vikings Creed

A Django web app for managing a university department's courses, sections and teaching assistant (TA) assignments. Built by team *Vikings Creed* (Sam, Milad, Jamie and turkogl3) as a semester-long, sprint-based software engineering project in spring 2022.

## Features

Three roles, each with its own view of the app:

| Role | Can do |
| --- | --- |
| **Supervisor** | Create, edit and delete accounts; create courses; assign instructors and TAs to courses; create sections |
| **Instructor** | View courses and sections; assign TAs to sections |
| **TA** | View the sections they are assigned to |

Plus for everyone:

- Session-based login
- Department-wide contact list
- "My sections" page

## Tech stack

- Python and Django 4.0
- SQLite
- Django templates (server-rendered HTML)
- `unittest` unit tests and Django `TestCase` acceptance tests

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (macOS/Linux: source .venv/bin/activate)
pip install "django>=4.0,<4.1"
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000 and log in. The repository includes a sample `db.sqlite3` with demo supervisor, instructor and TA accounts (for example `sup@email.com` is a supervisor).

## Tests

```bash
python manage.py test acceptance_tests     # end-to-end page tests with Django's test client
python -m unittest discover Unit_Tests     # domain class unit tests
```

## Project layout

```
project/            Django settings and URL routes
proj_app/           Models (users, courses, sections), views and migrations
classes/            Domain classes: User, Supervisor, Instructor, TA, Course, Section, Driver
templates/          HTML pages
static/             Images and static assets
acceptance_tests/   Acceptance tests for each user story
Unit_Tests/         Unit tests for the domain classes
Sprint 2 Doc.pdf    Sprint documentation
```

## Note

This is a class project and isn't production-ready: passwords are stored in plain text, the secret key is committed and `DEBUG` is on. Don't deploy it as-is.
