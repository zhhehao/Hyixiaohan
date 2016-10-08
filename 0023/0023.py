from flask import Flask, request, render_template
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def liuyan():
	if request.method == 'POST':
		username = request.form['username']
		message = request.form['message']
		return render_template('liuyan.html', username=username, message=message)
	else:
		return render_template('liuyan.html')

if __name__ == '__main__':
	app.run()
