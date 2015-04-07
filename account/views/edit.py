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


########################################################
###### Shows the list of users
@view_function
def process_request(request):
	params = {}

	if request.user.is_authenticated():
		all_users = hmod.User.objects.all().order_by('username') #.filter, .exclude, .get
		params['allusers'] = all_users

		return templater.render_to_response(request, 'account.edit.html', params)

	else:
	    # Do something for anonymous users.
		return HttpResponseRedirect('/homepage/anon_user/')


	# returns user objects and not the strings.

	########################################################
###### Edit a user

@view_function
def edit(request):
	params = {}
	#print('0:', request.urlparams[0])
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
		print(">>>>>>>>>>>>>>>>>>>>>>")
		print(">>>>>>>>>>>>>>>>>>>>>>", user.username)
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage')
	


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
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.first_name= form.cleaned_data['first_name']
			print(form.cleaned_data)
			#g = Group.objects.get(name=form.choices.cleaned_data)#cleaned_data['choices']) 
			#g.user_set.add(user)
			user.save()
			#l = request.user.groups.values_list('name',flat=True)
			#print('user is in groups:', l)
			return HttpResponseRedirect('/account/')


	params['form'] = form


	return templater.render_to_response(request, 'account.edit.html', params)



class UserEditForm(forms.Form):
	username = forms.CharField(label ="Username", required=True, max_length=100)
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
	
	print(">>>>>>>>>>>>>>>>>>>>>made new user")
	return HttpResponseRedirect('/account/edit.edit/'+str(user.id))