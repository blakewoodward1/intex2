from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod


templater = get_renderer('catalog')

@view_function
def process_request(request):
 

	params = {}
	
	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}
		request.session.modified=True
		print(">>>>>>>>>>>>>>>Shopping cart init'd")


	all_item = hmod.Sale_Item.objects.all()#filter(isRental = False) #.filter, .exclude, .get
	all_rental = hmod.Rentable_Item.objects.all()
	params['all_rentable'] = all_rental
	params['all_item'] = all_item
	

	return templater.render_to_response(request, 'index.html', params)


@view_function
def add_to_cart(request):
	params={}

	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}
	#request.session['shopping_cart'].append([item.id, 1])
	if item.id not in request.session['shopping_cart']:
		request.session['shopping_cart'][item.id]=1
	else:
		request.session['shopping_cart'][item.id] += 1	

@view_function
def query(request):
	params = {}
	keyword=request.urlparams[0]
	# all_item= hmod.Sale_Item.objects.raw('SELECT * from homepage_Sale_Item  where "id" == '+keyword)#WHERE "name" LIKE "musket"')#"musket" LIKE name')# LIKE  %'+keyword+'%')
	#params['all_item'] = hmod.Sale_Item.objects.raw("SELECT * from homepage_Sale_Item WHERE 'name' LIKE '%a%'")#%s', [keyword])
	sale_item=hmod.Sale_Item.objects.filter(name__icontains=keyword)
	# params['all_item_len']=len(list(all_item))
	#print(">>>>>>>>>;ljlkjlkjlkjljk>>>>>>>>>>>>>>>", params['all_item_len'])
	params['all_item']=sale_item 
	return templater.render_to_response(request, 'index.html', params)