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
	params = {}

	if request.user.is_authenticated():

		cart_items=[]
		cart_items=request.session['shopping_cart']#.keys()
		params['cart']=request.session['shopping_cart']

		all_items = hmod.Sale_Item.objects.all()
		params['all_items'] = all_items
		


		return templater.render_to_response(request, 'checkout.html', params)

	else:
	    # Do something for anonymous users.
		return HttpResponseRedirect('/homepage/anon_user/')
