from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms


templater = get_renderer('homepage')


########################################################
###### Shows the list of wardrobe
@view_function
def process_request(request):
	params = {}
	if request.user.is_authenticated():


		all_figure = hmod.Historical_Figure.objects.all() #.filter, .exclude, .get
		params['all_figure'] = all_figure
		

		return templater.render_to_response(request, 'historical_figure.html', params)
	else:
		return HttpResponseRedirect('/homepage/anon_user/')

	########################################################
###### Edit a Wardrobe

@view_function
def edit(request):
	if request.user.is_authenticated():
		params = {}

		try:
			figure = hmod.Historical_Figure.objects.get(id=request.urlparams[0])
		except hmod.Historical_Figure.DoesNotExist:
			return HttpResponseRedirect('/homepage/historical_figure/')
		

		form = FigureEditForm(initial={
			'name': figure.name,
			'birth_date':  figure.birth_date,
			'birth_place': figure.birth_place,
			'death_date': figure.death_date,
			'death_place': figure.death_place,
			'biographical_note': figure.biographical_note,
			'is_fictional': figure.is_fictional,
			})

		if request.method == 'POST':
			form = FigureEditForm(request.POST) #validation
			form.historical_figureid = figure.id
			if form.is_valid():
				figure.name = form.cleaned_data['name']
				figure.birth_date = form.cleaned_data['birth_date']
				figure.birth_place = form.cleaned_data['birth_place']
				figure.death_date= form.cleaned_data['death_date']
				figure.death_place= form.cleaned_data['death_place']
				figure.biographical_note = form.cleaned_data['biographical_note']
				figure.is_fictional =form.cleaned_data['is_fictional']
				figure.save()
				return HttpResponseRedirect('/homepage/historical_figure/')


		params['form'] = form

		return templater.render_to_response(request, 'historical_figure.edit.html', params)
	else:
		HttpResponseRedirect("/homepage/anon_user")


class FigureEditForm(forms.Form):
	name = forms.CharField(required=True, max_length=100)
	birth_date = forms.DateField(required=True)
	birth_place = forms.CharField(required=True)
	death_date = forms.DateField()
	death_place = forms.CharField()
	biographical_note = forms.CharField()
	is_fictional = forms.BooleanField(required=False)

	def clean_name(self):
		if len(self.cleaned_data['name']) <5:
			raise forms.ValidationError("Please a name greater than 5 characters.")
			figure_count = hmod.Historical_Figure.objects.filter(name=self.cleaned_data['name']).exclude(id=self.historical_figureid).count()
			if figure_count >=1:
				raise forms.ValidationError("This figure already exists in the databases")
		return self.cleaned_data['name']


@view_function
def create(request):
	'''creates a new user'''
	if request.user.is_authenticated():

		figure = hmod.Historical_Figure()
		figure.name = ''
		figure.birth_date ="2000-04-04"
		figure.birth_place = ''
		figure.death_date="2000-04-05"
		figure.death_place= ''
		figure.biographical_note = ''
		figure.is_fictional = True
		figure.save()

		return HttpResponseRedirect('/homepage/historical_figure.edit/{}'.format(figure.id))
	else:
		return HttpResponseRedirect("/homepage/anon_user")

@view_function
def delete(request):
	params = {}
	if request.user.is_authenticated():

		try:
			figure = hmod.Historical_Figure.objects.get(id=request.urlparams[0])
		except hmod.Historical_Figure.DoesNotExist:
			return HttpResponseRedirect('/homepage/historical_figure/')

		hmod.Historical_Figure.objects.get(id=request.urlparams[0]).delete()

		return HttpResponseRedirect('/homepage/historical_figure/')
	else:
		return HttpResponseRedirect("/homepage/anon_user")
