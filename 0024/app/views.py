from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Hao'}
	return render_template('index.html', user=user)
