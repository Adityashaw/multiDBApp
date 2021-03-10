"""
All views (routes) and associated functions are written here
"""

from flask import render_template
from multidbapp import app, db
from .models import Faculty, Student


@app.route('/')
def index():
    """
    Home Page
    don't know what's needed or not needed
    """
    return "Hello Team"


@app.route('/MySQL')
def showFaculties():
    faculties = Faculty.query.all()
    return render_template('showFaculties.html', faculties=faculties)


@app.route('/PostgreSQL')
def showStudents():
    students = Student.query.all()
    return render_template('showStudents.html', students=students)
