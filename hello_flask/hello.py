from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
	return render_template('index.html', name='Ethan')

@app.route('/success')
def success():
	return render_template('success.html')
app.run(debug=True)
