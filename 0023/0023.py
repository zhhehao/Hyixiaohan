from flask import Flask, request, render_template
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def liuyan():
	return render_template('liuyan.html')

if __name__ == '__main__':
	app.run()
