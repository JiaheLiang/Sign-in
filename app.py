from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from sqlalchemy.orm import sessionmaker
from data import *
engine = create_engine('sqlite:///base.db', echo=True)

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('login.html')
	
@app.route('/signup', methods=['POST', 'GET'])
def signup():
	
	POST_NAME = request.form['inputName']
	POST_PASSWORD = request.form['inputPassword']
	POST_EMAIL = request.form['inputEmail']
	POST_AGE = request.form['inputAge']
	
	if [POST_AGE] > '18':
		Session = sessionmaker(bind=engine)
		s = Session()
		result = s.query(Log).filter(Log.name.in_([POST_NAME]), Log.email.in_([POST_EMAIL]) )
		out = result.first()
		if out:
			flash('Username or email address already signup!!!!')
		else:
			log = Log([POST_NAME],[POST_PASSWORD],[POST_EMAIL],"user")
			session.add(log)
			session.commit()
			flash('You have been successful sign up')
	else:
		flash('Your must be older than 18')

@app.route('/login', methods=['POST', 'GET'])
def login():
	
	POST_USERNAME = request.form['inputName']
	POST_USERPASSWORD = request.form['inputPassword']
	
	Session = sessionmaker(bind=engine)
	s = Session()
	user = s.query(Log).filter(Log.name.in_([POST_USERNAME]), Log.password.in_([POST_USERPASSWORD]))
	test = user.first()
	if test.type == 'admin': 
		session['logged_in'] = True
		return render_template('admin.html')
	elif test.type == 'user':
		session['logged_in'] = True
		return render_template('user.html')
	else:
		flash('Wrong username or password')
		return main()

@app.route("/logout")
def logout():
	session['logged_in'] = False
	return main()
	
if __name__ == "__main__":
	app.run()