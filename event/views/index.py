from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist


templater = get_renderer('event')

@view_function
def process_request(request):
 

	params = {}
	template_vars = {}

	

	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}
		request.session.modified=True
		print(">>>>>>>>>>>>>>>Shopping cart init'd")


	all_event = hmod.Event.objects.all()#filter(isRental = False) #.filter, .exclude, .get
	#all_rental = hmod.Rentable_Item.objects.all()
	print(">>>>>>>EVENT>>>>>>>>>>>>>>>>>>", all_event)
	params['all_event'] = all_event
	

	return templater.render_to_response(request, 'index.html', params)

