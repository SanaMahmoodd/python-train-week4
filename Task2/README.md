## Task 2: Modules, Packages & Virtual Environments

### Goal
Refactor the student management system into a clean **Python package** and set up a reproducible development environment using a **virtual environment** and **dependency management**.

---

## What’s Included

### 1) Project structured as a package
The code is organized under a package named `school/`:

- `school/__init__.py`  
  Exposes main classes for easy imports (e.g., `from school import Student, Course`).
- `school/student.py`  
  Student model + GPA property + validation helpers.
- `school/course.py`  
  Course model (iterable + length support).
- `school/management.py`  
  `SchoolManager` to manage students (add/get/list).

### 2) Virtual Environment (venv)
A local environment is used to isolate dependencies:

- Folder: `.venv/` (ignored by Git)

### 3) Dependencies & requirements.txt
Dependencies are installed via `pip` and saved in:

- `requirements.txt`

### 4) Code Quality (flake8)
Static checks run successfully on project code:

```bash
flake8 school tests
```

### 5) Unit tests (pytest)
Basic tests ensure the package works as expected:

```bash
pytest -q
```

Current status: **All tests passing** ✅

---

## Repository Structure

```text
python-train-week4/
└── Task2/
    ├── school/
    │   ├── __init__.py
    │   ├── student.py
    │   ├── course.py
    │   └── management.py
    ├── tests/
    │   └── test_management.py
    ├── requirements.txt
    ├── .flake8
    └── README.md
```

---

## Setup & Run (Windows + Git Bash)

### 1) Create & activate venv
```bash
py -m venv .venv
source .venv/Scripts/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run lint + tests
```bash
flake8 school tests
pytest -q
```

---

## Notes
- `.venv/` should not be committed to GitHub.
- flake8 is configured to exclude `.venv` and caches via `.flake8`.

---

**Status:** Completed ✅
