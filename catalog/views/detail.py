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
	template_vars = {}

	print('>>>>>>>>>>>', request.session)
	print('>>>>>>>>>>>', request.urlparams[0])
	
	all_item = hmod.Sale_Item.objects.get(id=request.urlparams[0]) #.filter, .exclude, .get
	params['all_item'] = all_item
	

	return templater.render_to_response(request, 'detail.html', params)


