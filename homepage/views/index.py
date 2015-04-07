from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login, logout


templater = get_renderer('homepage')

@view_function
def process_request(request):
	template_vars = {}

	print('>>>>>>>>>>>', request.session)
	request.session['hey'] = 'world'
	print('>>>>>>>>>>', request.session['hey'])
	

	'''###################Shopping Cart ##############
	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}
	#request.session['shopping_cart'].append(item.id)

	if item.id not in request.session['shopping_cart']:
		request.session['shopping_cart'][item.id]=1
	else: 
		request.sessio['shopping_cart'][item.id] +=1

	print('>>>>>>>>>>>>>', request.session['shopping_cart'])'''


	return templater.render_to_response(request, 'index.html', template_vars)


