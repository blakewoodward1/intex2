from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required


templater = get_renderer('account')



@view_function
def create(request):
	'''creates a new user'''
	user = hmod.User()
	user.username = ''
	user.password =''
	user.first_name = ''
	user.last_name=''
	user.phone = ''
	user.save()
	

	return HttpResponseRedirect('/edit/'.format(user.id))