# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash(u"Email cannot be blank!","error")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['firstname']) < 1:
        flash("Firstname cannot be blank")
    elif not name_regex.match(request.form['firstname']):
        flash("Invalid First Name")
    if len(request.form['lastname']) < 1:
        flash("Lastname cannot be blank")
    elif not name_regex.match(request.form['lastname']):
        flash("Invalid Last Name")
    if len(request.form['password']) < 1:
        flash("Password cannot be blank")
    elif len(request.form['password']) > 8:
        flash("Password cannot be longer than 8 characters")
    if len(request.form['password1']) < 1:
        flash("please enter your password again")
    if request.form['password'] != request.form['password1']:
        flash("please enter a matching password")

    return redirect('/')
app.run(debug=True)
