from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'ulist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('login.html')
@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputName']
        _password = request.form['inputPassword']
               
        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin',(_username,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][3]),_password):
                session['user'] = data[0][0]
                return redirect('/user')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')          

    except Exception as e:
        return render_template('sign.html',error = str(e))
    finally:
        cursor.close()
        con.close()
	
@app.route('/showSignup')
def showSignup():
    return render_template('sign.html')
@app.route('/signup',methods=['POST','GET'])
def signup():
	try:
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		_age = request.form['inputAge']
		if _age < 18:
			return rendere_template['errorage.html']
		elif _name and _email and _password and _age:
			conn = mysql.connect()
			cursor = conn.cursor()
			hashed_password = generate_password_hash(_password)
			cursor.callproc('sp_createUser',(_name,_email,_hashed_password,_age))
			data = cursor.fetchall()
			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':'User created successfully !'})
				return main()
			else:
				return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cursor.close() 
		conn.close()

@app.route('/user')
def user():
    return render_template('user.html')		

@app.route('/logout')	
def logout():
    session.pop('user', None)
    return redirect('/')
	
if __name__ == "__main__":
    app.run()