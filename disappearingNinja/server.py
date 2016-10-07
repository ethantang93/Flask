from flask import Flask, render_template, session, redirect, request, flash
app= Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def noninja():
    return "No ninjas here"

@app.route('/ninja')
def fourninjas():
    return render_template('fourninjas.html')
@app.route('/ninja/<color>')
def colorninjas(color):
    if color == "blue":
        imgname= "leonardo.jpg"
    elif color == "orange":
        imgname= "michelangelo.jpg"
    elif color == "red":
        imgname= "raphael.jpg"
    elif color == "purple":
        imgname= "donatello.jpg"
    else :
        imgname= "notapril.jpg"
    return render_template('oneninja.html',imgname=imgname)

app.run(debug=True)
