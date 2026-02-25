from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []  # list of dicts: {"name": "...", "student_id": "..."}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        student_id = request.form.get("student_id", "").strip()

        # validation
        errors = []
        if not name:
            errors.append("Name is required.")
        if not student_id:
            errors.append("Student ID is required.")

        # condition (Jinja) + check duplicates
        if student_id and any(s["student_id"] == student_id for s in students):
            errors.append("Student ID already exists.")

        if errors:
            return render_template(
                "register.html",
                errors=errors,
                old={"name": name, "student_id": student_id},
            )

        students.append({"name": name, "student_id": student_id})
        return redirect(url_for("student_list"))

    # GET
    return render_template("register.html", errors=[], old={"name": "", "student_id": ""})


@app.route("/students")
def student_list():
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)