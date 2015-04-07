from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod


templater = get_renderer('event')

@view_function
def process_request(request):


	params = {}
	template_vars = {}

	print('>>>>>>>>>>>', request.session)
	print('>>>>>>>>>>>', request.urlparams[0])
	
	product=hmod.Sale_Item.objects.filter(isRental=False)
	event = hmod.Event.objects.get(id=request.urlparams[0]) #.filter, .exclude, .get
	params['event'] = event
	
	products = []
	i=0

	while len(products)<4:
		randProd = random.choice(product)
		if randProd not in products:
			products.append(randProd)

	# for i in range(3):
	# 	randProd = random.choice(product)
	# 	if randProd not in products:
	# 		products.append(randProd)
	params['products']=products


	return templater.render_to_response(request, 'detail.html', params)


