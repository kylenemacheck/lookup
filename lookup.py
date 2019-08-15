import mysql.connector

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__, static_url_path="/static", static_folder="templates")

@app.route('/')
def index():
	return render_template('lookup.html')

@app.route('/lookup')
def thing():
	conn = mysql.connector.connect(host="localhost", user="student", passwd="fredfredburger", database="nations")
	cursor = conn.cursor()
	cursor.execute("SELECT name, pop FROM nations WHERE name like '%s'" % ('%'+request.args.get('inputText')+'%'))
	a = ''
	for i in cursor.fetchall():
		a = a + str(i) + '<br>'
	return a 

if __name__ == '__main__':
	app.run('198.110.204.9', 5000, debug = True)
