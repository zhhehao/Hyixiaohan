from app import db

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True)
	content = db.Column(db.String(400), index=True)

	def __init__(self, title, content):
		self.title = title
		self.content = content

	def __repr__(self):
		return '<Tod %r>' % self.title
