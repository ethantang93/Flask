from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

def farm():
    return random.randrange(10,21)
def cave():
    return random.randrange(5,11)
def house():
    return random.randrange(2,6)
def casino():
    return random.randrange(-50,50)

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['gold']=0
    number=0
    session['activity_log']=[]
    return render_template('index.html', number = number)


@app.route('/process_money', methods=['POST'])
def process_money():
    selection=str(request.form['building'])
    print selection
    log_entry=""
    number = 0
    if selection == "farm":
        gold = farm()
        session['gold'] += gold
        log_entry="Earned {} gold from the farm".format(gold)
    elif selection =="cave":
        gold = cave()
        session['gold'] += gold
        log_entry="Earned {} gold from the cave".format(gold)
    elif selection =="house":
        gold = house()
        session['gold'] += gold
        log_entry="Earned {} gold from the house".format(gold)
    elif selection =="casino":
        gold = casino()
        session['gold'] += gold
        if gold >0 :
            log_entry="Earned {} gold from the casino".format(gold)
        else:
            log_entry="lost {} gold from the casino".format(abs(gold))
    log_entry = log_entry+str(datetime.now())[:20]
    session['activity_log'].append(log_entry)
    number=len(session['activity_log'])
    print number
    print session['activity_log']
    return render_template('index.html', activity_log=session['activity_log'], number = number)


app.run(debug=True)
