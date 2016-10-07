from flask import Flask, render_template, request, redirect, session
import random

def random_gen():
    return random.randrange(0,101)

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['real_number']=random_gen()
    print session['real_number']
    session['color']=""
    session['words']=""
    session['play']=""
    session['hideit']="hidden"
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    guess_number=int(request.form['guess_number'])
    number = int(session['real_number'])
    print guess_number
    print number
    if guess_number>number:
        session['words']="Too High"
        session['color']='red'
        session['play']=""
        session['hideit']="hidden"
        return render_template('index.html')
    elif guess_number<number:
        session['words']="Too Low!!!"
        session['color']='red'
        session['play']=""
        session['hideit']="hidden"
        return render_template('index.html')
    elif guess_number==number:
        session['words']="You are correct"
        session['color']='green'
        session['play']="PlayAgain!"
        session['hideit']="submit"
        return render_template('index.html')
@app.route('/replay', methods=['POST'])
def replay():
    session.pop('real_number')
    session['real_number']=random_gen()
    return redirect('/')
app.run(debug=True)
