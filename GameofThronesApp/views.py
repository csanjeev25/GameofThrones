from django.shortcuts import render
import cx_Oracle
from django.http import HttpResponse
from .models import House
from .models import Character
from .models import Battle

# Create your views here.

def index(request):
	'''con = cx_Oracle.connect('system/oracle@127.0.0.1:1521/xe')
	cur = con.cursor()
	cur.execute('SELECT * from battle')
	result = cur.fetchall()
	return HttpResponse("Valar Morghulis")'''
	houses = House.objects.all()
	return render(request,'index.html',{'houses':houses})

def house(request,pk):
	house = House.objects.get(pk=pk)
	return render(request,'house.html',{'house':house})

def character(request,pk):
	try:
		character = Character.objects.get(pk=pk)
	except Character.DoesNotExist:
		raise Http404
	return render(request,'character.html',{'character':character})

def new_character(request,pk):
	try:
		character = Character.objects.get(pk=pk)
	except Character.DoesNotExist:
		raise Http404
	return render(request,'new_character.html',{'character':character})

def new_house(request,pk):
	try:
		house = House.objects.get(pk=pk)
	except House.DoesNotExist:
		raise Http404
	return render(request,'new_house.html',{'house':house})

def new_battle(request,pk):
	try:
		battle = Battle.objects.get(pk=pk)
	except Battle.DoesNotExist:
		raise Http404
	return render(request,'new_battle.html',{'battle':battle})

