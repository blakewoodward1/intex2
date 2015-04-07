from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod

templater = get_renderer('homepage')

@view_function
def process_request(request):
 
	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}
		request.session.modified=True
		print(">>>>>>>>>>>>>>>Shopping cart init'd")