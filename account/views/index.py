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


templater = get_renderer('account')

@view_function
def process_request(request):
	params = {} 

	if request.user.is_authenticated():
	    # Do something for authenticated users.
		print(">>>>>>>>>>>>>>>>>>>>", request.user.id)
		try:
			active_user = hmod.User.objects.get(id=request.user.id)
		except ObjectDoesNotExist:
			return HttpResponseRedirect('/homepage')
		params['activeUser'] = active_user
		return templater.render_to_response(request, 'index.html', params)

	else:
	    # Do something for anonymous users.
		print("not authenticated")
		return HttpResponseRedirect('/homepage/anon_user/')







@view_function
def edit(request):
	params = {}
	#print('0:', request.urlparams[0])
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/account')
	


	form = UserEditForm(initial={
		'username':  user.username,
		'first_name': user.first_name,
		'last_name':  user.last_name,
		'email': user.email,
		})

	if request.method == 'POST':
		form = UserEditForm(request.POST)
		form.userid=user.id #validation
		if form.is_valid():
			print(form.cleaned_data)
			user.username = form.cleaned_data['username']
			user.password = form.cleaned_data['password']
			user.set_password(user.password)
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.first_name= form.cleaned_data['first_name']
			print(form.cleaned_data)
			#g = Group.objects.get(name=form.choices.cleaned_data)#cleaned_data['choices']) 
			#g.user_set.add(user)
			user.save()
			#l = request.user.groups.values_list('name',flat=True)
			#print('user is in groups:', l)
			return HttpResponseRedirect('/homepage/users/')


	params['form'] = form


	return templater.render_to_response(request, 'users.edit.html', params)



class UserEditForm(forms.Form):
	username = forms.CharField(label ="Put the username", required=True, max_length=100)
	password = forms.CharField(required=True, max_length=128)
	first_name=forms.CharField(required=True, max_length=100)
	last_name = forms.CharField(required=True, max_length=100)
	email= forms.EmailField(required=True, max_length=100)



	def clean_username(self):
		if len(self.cleaned_data['username']) <5:
			raise forms.ValidationError("Please a username greater than 5 characters.")
		user_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if user_count >=1:
			raise forms.ValidationError("This username is not free")
		
		return self.cleaned_data['username']


class PasswordForm(forms.Form):
	password = forms.CharField(label ="New password",  required=True, max_length=128, widget=forms.PasswordInput)
	password_confirm = forms.CharField(label = "Confirm password",  required=True, max_length=128, widget=forms.PasswordInput)

	def clean(self):
		password1=self.cleaned_data['password']
		password2=self.cleaned_data['password_confirm']

		if password2 == password1:
			return password1#self.cleaned_data['password']
		else:
			raise forms.ValidationError("Passwords must match.")


@view_function
def passwordForm(request):
	active_user = hmod.User.objects.get(id=request.user.id)
	template_vars = {}
	form = PasswordForm()
	if request.method == "POST":
		form=PasswordForm(request.POST)
		if form.is_valid():
			password3 = form.cleaned_data
			active_user.set_password(password3)
			active_user.save()
			active_user = authenticate(username=request.user.username, password=password3)
			login(request, active_user)


			return HttpResponse('<script> window.location.reload();</script>')

	template_vars['form'] = form
	return templater.render_to_response(request, 'passwordForm.html', template_vars)