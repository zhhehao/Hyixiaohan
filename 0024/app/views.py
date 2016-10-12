from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Hao'}
	flash('This is a flash message test.')
	return render_template('index.html', user=user)
