#!/usr/bin/env python35
# -*- coding: utf-8 -*-

import os
import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template
import datetime

# Create flask instance
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config
app.config.update(dict(
		DATABASE=os.path.join(app.root_path, '0023.db'),
		SECRET_KEY='\x00\xd8h(Z\x17\x8d\xb5\x97l\x88x0\xf2\xb3\xdcfU\xdb\x1f\x8d\x0b\xafk'
	))
app.config.from_envvar('0023_SETTINGS', silent=True)

# Connect to database
def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

# Open database connection
def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

# Close database at the end of request
@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

# Init database
def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('Initialized the database.')

# Show entries
@app.route('/')
def show_entries():
	db = get_db()
	cur = db.execute('select title, date, text from entries order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries)

# Add entry
@app.route('/add', methods=['POST'])
def add_entry():
	submit_time = str(datetime.datetime.now())
	db = get_db()
	db.execute('insert into entries (title, date, text) values (?, ?, ?)', \
		[request.form['title'], submit_time, request.form['text']])
	db.commit()
	return redirect(url_for('show_entries'))

