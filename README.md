# Python Training - Week 4 🚀

## Overview

This repository contains advanced Python and Flask training tasks
completed during Week 4.

Each task is designed to take between half a day to a full day and
focuses on practical implementation.

------------------------------------------------------------------------

## Task 1 -- Python Advanced Features

### Topics Covered

-   Static Methods (`@staticmethod`)
-   Class Methods (`@classmethod`)
-   Properties (`@property`, `@setter`)
-   Special Methods:
    -   `__len__`
    -   `__eq__`
    -   `__iter__`

### Implementation

-   Created a `Student` class with:
    -   GPA auto-calculated using `@property`
    -   Equality comparison based on `student_id`
-   Created a `Course` class with iterable behavior:
    -   Enables: `for student in course:`
    -   Supports `len(course)`

------------------------------------------------------------------------

## Task 2 -- Modules, Packages & Virtual Environments

-   Project structured into a Python package (`school/`)
-   Usage of `__init__.py`
-   Dependency management with `pip` and `requirements.txt`
-   Added `pytest` and `flake8`

------------------------------------------------------------------------

## Task 3 -- Flask Introduction

-   Created basic Flask application
-   Implemented routes:
    -   `/`
    -   `/hello/<name>`
-   Added `.gitignore`
-   Pushed project to GitHub

------------------------------------------------------------------------

## Task 4 -- Flask Templates & Forms

-   Used Jinja2 templates
-   Built student registration form
-   Stored students in in-memory list
-   Rendered student list page

------------------------------------------------------------------------

## Task 5 -- Flask Student Portal (Mini Project)

Features: 
- Homepage with navigation 
- Student registration (POST) 
- Student list (GET) 
- Individual student details page 
- Basic unit tests using Flask test client

------------------------------------------------------------------------

## Author
Sana Saleh