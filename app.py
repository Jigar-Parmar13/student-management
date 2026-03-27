from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory student data (no database needed)
students = [
    {"id": 1, "name": "Aarav Shah", "age": 20, "course": "Computer Science", "grade": "A"},
    {"id": 2, "name": "Priya Patel", "age": 22, "course": "Data Science", "grade": "B+"},
    {"id": 3, "name": "Rohan Mehta", "age": 21, "course": "Web Development", "grade": "A-"},
]
next_id = 4

@app.route("/")
def index():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    global next_id
    student = {
        "id": next_id,
        "name": request.form["name"],
        "age": int(request.form["age"]),
        "course": request.form["course"],
        "grade": request.form["grade"],
    }
    students.append(student)
    next_id += 1
    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>")
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return redirect(url_for("index"))

@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        return redirect(url_for("index"))
    if request.method == "POST":
        student["name"] = request.form["name"]
        student["age"] = int(request.form["age"])
        student["course"] = request.form["course"]
        student["grade"] = request.form["grade"]
        return redirect(url_for("index"))
    return render_template("edit.html", student=student)

@app.route("/health")
def health():
    return jsonify({"status": "ok", "total_students": len(students)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
