import hashlib

db = {}

def get_sha1(password):
	sha1 = hashlib.sha1()
	sha1.update(password.encode('utf-8'))
	return sha1.hexdigest()

def register(username, password):
	db[username] = get_sha1(password+username+password)

def login(username, password):
	if username not in db:
		print('Wrong username!')
	elif db[username] != get_sha1(password+username+password):
		print('Wrong password!')
	else:
		print('Login successfully!')

register('zhangshan', '1234567')
register('lisi', 'ABCDEFG')
register('wangwu', 'fd98safjdsal')

login('zhangsshan', '1234567')
login('lisi', 'abcdefg')
login('wangwu', 'fd98safjdsal')
