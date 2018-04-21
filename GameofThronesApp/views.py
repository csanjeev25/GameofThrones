from django.shortcuts import render
import cx_Oracle
from django.http import HttpResponse
from .models import House

# Create your views here.

def index(request):
	'''con = cx_Oracle.connect('system/oracle@127.0.0.1:1521/xe')
	cur = con.cursor()
	cur.execute('SELECT * from battle')
	result = cur.fetchall()
	return HttpResponse("Valar Morghulis")'''
	houses = House.objects.all()
	return render(request,'index.html',{'houses':houses})