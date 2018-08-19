from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from sqlalchemy.orm import sessionmaker
from table import *
engine = create_engine('sqlite:///data.db', echo=True)

app = Flask(__name__)


@app.route('/')
def main():
	return render_template('new.html')

@app.route('/input', methods=['GET', 'POST'])
def importuser():
	
	POST_NAME = request.form['username']
	POST_GENDER = request.form['gender']
	
	Session = sessionmaker(bind=engine)
	s = Session()
	frs = s.query(User).filter(User.name.in_([POST_NAME]), User.gender.in_([POST_GENDER]))
	out = frs.first()
	results = s.query(User).filter(User.gender != out.gender, User.address == out.address)
	result = results.first()
	if results:
		return "Name: " + result.name + " Address: " + result.address
	else:
		return "Object not found"

if __name__ == "__main__":
	app.run()
		
	