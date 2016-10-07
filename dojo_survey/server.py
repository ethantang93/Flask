from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key='thisisasecretkey'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name= request.form['name']
    session['name']=name
    comment = request.form['comment']
    session['comment']=comment
    session['location'] = request.form['location']
    session['language'] = request.form['lang']
    if len(name)< 1 :
        flash("name must not be empty")
        return redirect('/')
    elif len(comment) <1:
        flash("comments must not be empty")
        return redirect('/')
    elif len(comment) >120 :
        flash("comments must be less than 120 words")
        return redirect('/')
    else:
        flash("success")
        return redirect('/result')
@app.route('/result', methods=['get'])
def result():
    print "got the user input"
    name = session['name']
    print name
    location = session['location']
    print location
    lang = session['language']
    print lang
    comment= session['comment']
    print comment
    return render_template('result.html', name = name, location = location, lang = lang, comment= comment)
app.run(debug=True)
