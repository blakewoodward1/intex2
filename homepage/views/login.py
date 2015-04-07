from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login, logout


templater = get_renderer('homepage')

#######################################################
###### Edit a user

@view_function
def process_request(request):
	params = {}
	#print('0:', request.urlparams[0])

	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			login(request, user)
			l = request.user.groups.values_list('name',flat=True)
			print('user is in groups:', l)

			return HttpResponseRedirect('/homepage/')


	params['form'] = form
	return templater.render_to_response(request, 'login.html', params)



class LoginForm(forms.Form):
	username = forms.CharField(label ="Username",  required=True, max_length=100)
	password = forms.CharField(label = "Password",  required=True, max_length=128, widget=forms.PasswordInput)

	def clean(self):
		netid=self.cleaned_data.get('username')
		pw = self.cleaned_data.get('password')
		from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO, SEARCH_SCOPE_WHOLE_SUBTREE
		s = Server('chfgroup.us', port=3890, get_info = GET_ALL_INFO)

		try:
			user = authenticate(username=self.cleaned_data.get('username',''), password=self.cleaned_data.get('password',''))
			if user == None:
				raise forms.ValidationError("You don't get to come in")
			return self.cleaned_data
		except:
			raise forms.ValidationError("Errors")




from django.contrib.auth import logout

@view_function
def logout_view(request):
	params = {}
	logout(request)
	return HttpResponseRedirect('/homepage/')


@view_function
def loginform(request):
  template_vars = {}
  form = LoginForm()
  if request.method == "POST":
    form=LoginForm(request.POST)
    if form.is_valid():
   
      user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      login(request, user)
      l = request.user.groups.values_list('name',flat=True)
      print('>>>>>>>>>>>>>user is in groups:', l)

      return HttpResponse('''
      	<script> window.location.reload();</script>

      ''')


  template_vars['form'] = form
  return templater.render_to_response(request, 'login.loginform.html', template_vars)