# Python Training -- Week 4

## Task 3: Flask Introduction 🚀

------------------------------------------------------------------------

## What is Flask?

Flask is a **lightweight Python web framework** used to build web
applications.

### Why is it called lightweight?

-   Minimal and simple core
-   No built‑in database or complex structure forced on you
-   Easy to start with (single file app possible)
-   Flexible and extensible

Flask gives you the basics and lets you decide how complex your project
becomes.

------------------------------------------------------------------------

## Task Objective

-   Create a basic Flask application
-   Understand routing using `@app.route`
-   Learn the difference between GET and POST
-   Run the app locally
-   Manage dependencies using `requirements.txt`

------------------------------------------------------------------------

## 🗂 Project Structure

``` text
python-train-week4/
└── Task3/
    ├── app.py
    ├── requirements.txt
    └── README.md
```

------------------------------------------------------------------------

## Understanding the Code

### app.py

``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask! ✅"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}! 👋"

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation

-   `Flask(__name__)` → creates the application
-   `@app.route("/")` → defines a route (URL)
-   `/hello/<name>` → dynamic route (accepts variable)
-   `debug=True` → auto-reload + debugging mode

------------------------------------------------------------------------

## Routes Implemented

### 1️⃣ Home Route

    /

Returns:

    Welcome to Flask! ✅

### 2️ Dynamic Route

    /hello/<name>

Example:

    /hello/Sana

Returns:

    Hello, Sana! 👋

------------------------------------------------------------------------

## GET vs POST

### GET

-   Used to retrieve data
-   Triggered when visiting a URL in browser
-   Both routes in this task use GET

### POST

-   Used to send data (forms, login, etc.)
-   Will be implemented in Task 4

------------------------------------------------------------------------

## How to Run

### 1️⃣ Activate Virtual Environment

``` bash
source ../.venv/Scripts/activate
```

### 2️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

``` bash
python app.py
```

Open in browser:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

**Status: Completed Successfully 🎉**