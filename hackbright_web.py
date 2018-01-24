"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def homepage():
    """Homepage."""

    return render_template("homepage.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html", first=first, last=last,
                           github=github, grades=grades)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student.  """

    return render_template("student_search.html")


@app.route("/student-add")
def new_student_form():
    """From to add to new students."""

    return render_template("add_student.html")


@app.route("/student-add", methods=["POST"])
def student_add():
    """Add a student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("display_new_student.html", first=first_name, last=last_name, github=github)

@app.route("/project")
def projects():
    """Show project description"""

    title = request.args.get('title')

    title, desc, max_grade = hackbright.get_project_by_title(title)

    grades = hackbright.get_grades_by_title(title)

    # acct, grade = assignment

    # first_name, last_name, acct = hackbright.get_student_by_github(acct)

    return render_template("project.html", title=title, desc=desc, max_grade=max_grade,
                            grades=grades)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
