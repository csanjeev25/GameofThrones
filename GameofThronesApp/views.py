from django.shortcuts import render
import cx_Oracle
from django.http import HttpResponse

# Create your views here.

def index(request):
	con = cx_Oracle.connect('system/oracle@127.0.0.1:1521/xe')
	cur = con.cursor()
	cur.execute('SELECT * from battle')
	result = cur.fetchall()
	return HttpResponse("Valar Morghulis")