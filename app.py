from flask import Flask, flash, render_template, request, redirect, session, url_for
from db import Add_contact
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form['email']
        message = request.form['message']
        Add_contact(name, email, message)
        return redirect('/')
    return render_template('index.html')

@app.route('/project1')
def project1():
    return render_template('project/project1.html')

@app.route('/project2')
def project2():
    return render_template('project/project2.html')

@app.route('/project3')
def project3():
    return render_template('project/project3.html')


if __name__ == "__main__":
    app.run(debug=True)