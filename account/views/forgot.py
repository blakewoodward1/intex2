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
from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import hashlib


templater = get_renderer('account')


class EmailForm(forms.Form):
	email_address = forms.EmailField(label='Email', max_length=100)





@view_function
def process_request(request):
	params = {} 

	form = EmailForm()
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			params['status'] = 'sent'			
			return HttpResponseRedirect('/account/forgot')
	params['form'] = form
	
	return templater.render_to_response(request, 'forgot.html', params)


@view_function
def reset(request):
	params = {} 
	if request.method == 'POST':
		form = EmailForm(request.POST)

		if form.is_valid():
			try:
				user = hmod.User.objects.get(email=form.cleaned_data['email_address'])
			except hmod.User.DoesNotExist:
				params['status'] = 'bad_user'
				return templater.render_to_response(request, 'forgot.html', params)	

			html_cont = get_template('email_forgot.html')

			m=hashlib.md5()
			m.update(user.password.encode('utf-8'))

			d = Context({'username': user.username, 'id': user.id, 'reset_code': m.hexdigest(), 'first_name': user.first_name })

			user.pass_exp = datetime.now() + timedelta(days=1)
			user.save()
			msg = EmailMultiAlternatives(
    		'Recover Password',
		    'Content goes here.',
		    'chf2-14@outlook.com',
		    [form.cleaned_data['email_address']]
		    #['theyhaveescaped@gmail.com'],
		    )
			html_content = html_cont.render(d)

			msg.attach_alternative(html_content, "text/html")
			#msg.attach_alternative(get_template('email_forgot.html').render(Context()), "text/html")
			msg.send()

			params['status'] = 'sent'

		return templater.render_to_response(request, '/forgot.html/', params)
			
	else: 
		form = EmailForm()
		
		return HttpResponseRedirect('/forgot.html')



class PasswordForm(forms.Form):
	password = forms.CharField(label ="New password",  required=True, max_length=128, widget=forms.PasswordInput)
	password_confirm = forms.CharField(label = "Confirm password",  required=True, max_length=128, widget=forms.PasswordInput)

	def clean(self):
		password=self.cleaned_data.get('password')
		password_confirm=self.cleaned_data.get('password_confirm')
		# if password2 == "":
		# 	raise forms.ValidationError("Password cannot be blank")
		# else:
		print(">>>>>>>>>>>>>>>Cleaning>>>>>>>>>>>>>>>>", password, password_confirm)
		if password_confirm == password:
			return password#self.cleaned_data['password']
		else:
			raise forms.ValidationError("Passwords must match.")


@view_function
def new_password(request):
	params = {} 
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
		m=hashlib.md5()
		m.update(user.password.encode('utf-8'))

		if m.hexdigest() != request.urlparams[1]:
			params['status'] = 'bad_hash'
			return templater.render_to_response(request, '/forgot.html/', params)
		if user.pass_exp < datetime.today().date():
			params['status'] = 'bad_hash'
			return templater.render_to_response(request, '/forgot.html/', params)

	except:
		pass

	else:
		form=PasswordForm()
		params['form']=form
		params['status'] = 'new_password'
		params['hash'] = request.urlparams[1]
		params['userid'] = request.urlparams[0]


		return templater.render_to_response(request, '/forgot.html/', params)

@view_function
def changePW(request):
	user = hmod.User.objects.get(id=request.urlparams[0])

	params={}
	form=PasswordForm()
	if request.method == "POST":
		form=PasswordForm(request.POST)
		if form.is_valid():
			password3 = form.cleaned_data
			print(">>>>>>>>>>>>>>>>>VALID>>>>>>>>>", password3)
	#return templater.render_to_response(request, '/forgot.html/', params)

			user.set_password(password3)
			user.save()
			active_user = authenticate(username=user.username, password=password3)
			login(request, active_user)
			return HttpResponseRedirect('/homepage/login/')
	# 	return templater.render_to_response(request, '/homepage/login', params)

	# 	params['form'] = form
	params['form'] = form

	# params['userid'] = user.id
	# params['hash'] = request.urlparams[1]
	params['status'] = 'new_password'
	params['hash'] = request.urlparams[1]
	params['userid'] = request.urlparams[0]
	return templater.render_to_response(request, '/forgot.html', params)


