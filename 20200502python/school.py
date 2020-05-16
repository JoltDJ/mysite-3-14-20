from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

students = {
    's01': 
  {
    'name': 'Jimmy', 
    'intro': 'Hello, I am Jimmy.',
    'avatar': '/static/img/avatars/avatar-1.webp'
  },
    's02': 
  {
    'name': 'Anthony', 
    'intro': 'Hello, I am Anthony.',
    'avatar': '/static/img/avatars/avatar-2.png'
  },
    's03': 
  {
    'name': 'Jacob', 
    'intro': 'Hello, I am Jacob.',
    'avatar': '/static/img/avatars/avatar-3.png'
  },
    's04': 
  {
    'name': 'Sally', 
    'intro': 'Hello, I am Sally.',
    'avatar': '/static/img/avatars/avatar-4.jpg'
  },
    's05': 
  {
    'name': 'Billy', 
    'intro': 'Hello, I am Billy.',
    'avatar': '/static/img/avatars/avatar-5.png'
  }
}

@app.route('/')
def school():
    return render_template("school.html", students=students)

@app.route('/student/<sid>')
def student(sid):
    student = students[sid]
    return render_template("student.html", student=student)