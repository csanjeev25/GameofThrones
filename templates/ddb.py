import cx_Oracle
from flask import Flask,render_template,url_for,request

app = Flask(__name__)

app.route('/')
def main():
	conn = cx_Oracle.connect("system/oracle@127.0.0.1:1521/xe")
	cur = con.cursor()
	cur.execute("SELECT * FROM character")
	character = cur.fetchall()
	cur.execute("SELECT * FROM house")
	house = cur.fetchall()
	cur.execute("SELECT * FROM battle")
	battle = cur.fetchall()





