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
	
	print(">>>>>>>>REDIRECTING TO HTML>>>>>>>>>>")

	return templater.render_to_response(request, 'rest.html', params)

