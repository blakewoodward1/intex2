from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod


templater = get_renderer('catalog')

@view_function
def process_request(request):
	params ={}
	#print(">>>>>>>>>asdf>>>>>>>>>>>>>", request.session['shopping_cart'])
	cart_items=[]
	cart_items=request.session['shopping_cart']#.keys()
	params['cart']=request.session['shopping_cart']
	all_items = hmod.Sale_Item.objects.all()
	params['all_items'] = all_items


	
	return templater.render_to_response(request, 'shopping_cart.html', params)


@view_function
def add(request):
	#del request.session['shopping_cart']
	params={}
	pid = str(request.urlparams[0])
	qty = request.urlparams[1]
	item = hmod.Sale_Item.objects.get(id=pid)
	if item.isRental:
		days = request.urlparams[2]

	alist =[]

	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = []
		request.session.modified=True
		print(">>>>>>>>>>>>>>>Shopping cart init'd")

	if pid in request.session['shopping_cart'].keys():
		print(">>>>>>>>>>>>>>>.>>>>>>>>>>>>", request.session['shopping_cart'] )
		alist.append(qty)
		if item.isRental:
			alist.append(days)
		request.session['shopping_cart'][pid] = alist
		request.session.modified=True

	else:
		print(">>>>>>>>>>.>>>>>>>>>>>>>>>>>", request.session['shopping_cart'] )
		alist.append(qty)
		if item.isRental:
			alist.append(days)
		request.session['shopping_cart'][pid]=alist
		request.session.modified=True
		print(">>>>>>>>>>>>>>>>>>it wasn't in before")

	request.session['shopping_cart']
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>", request.session['shopping_cart'] )

	return HttpResponseRedirect('/catalog/shopping_cart/')



@view_function
def delete(request):
  params={}
  pid = request.urlparams[0]
  del request.session['shopping_cart'][pid]
  request.session.modified=True
  return HttpResponseRedirect('/catalog/shopping_cart/')



