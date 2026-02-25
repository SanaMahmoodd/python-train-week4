# Python Training -- Week 4

## Task 4: Flask Templates & Forms

------------------------------------------------------------------------

## Overview

This task extends the basic Flask application by introducing:

-   Jinja2 templates
-   HTML forms
-   GET vs POST handling
-   In-memory data storage
-   Clean minimal CSS styling

The application now behaves like a small student portal.

------------------------------------------------------------------------

## Features Implemented

### 1. Templates (Jinja2)

Templates are stored inside the `templates/` folder.

Used concepts: - Variables: `{{ variable }}` - Loops:
`{% for item in list %}` - Conditions: `{% if condition %}` -
`loop.index` inside tables

------------------------------------------------------------------------

### 2. Student Registration Form

Route: /register

-   Supports GET (display form)
-   Supports POST (submit form data)
-   Basic validation:
    -   Name required
    -   Student ID required
    -   Student ID must be unique

------------------------------------------------------------------------

### 3. In-Memory Storage

Students are stored in a Python list:

students = \[\]

Data resets when the server restarts.

------------------------------------------------------------------------

### 4. Student List Page

Route: /students

-   Displays all registered students
-   Uses Jinja loop to render table
-   Shows message if list is empty

------------------------------------------------------------------------

## How to Run

1.  Activate Virtual Environment

source ../.venv/Scripts/activate

2.  Install Dependencies

pip install -r requirements.txt

3.  Run the App

python app.py

Open in browser: http://127.0.0.1:5000/

------------------------------------------------------------------------

## Learning Outcomes

-   Serving HTML templates with Flask
-   Handling forms using GET and POST
-   Using Jinja2 templating engine
-   Basic UI styling with CSS
-   Managing routes in Flask

------------------------------------------------------------------------

Status: Completed Successfully