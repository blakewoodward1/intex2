from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
import datetime

templater = get_renderer('homepage')


########################################################
###### Shows the list of wardrobe
@view_function
def process_request(request):
	params = {}


	all_wardrobe = hmod.Wardrobe_Item.objects.all() #.filter, .exclude, .get
	params['all_wardrobe'] = all_wardrobe
	

	return templater.render_to_response(request, 'wardrobe.html', params)


	########################################################
###### Edit a Wardrobe

@view_function
def edit(request):
	params = {}

	try:
		wardrobe = hmod.Wardrobe_Item.objects.get(id=request.urlparams[0])
	except hmod.Wardrobe_Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/wardrobe/')
	

	form = WardrobeEditForm(initial={
		'name': wardrobe.name,
		'size': wardrobe.size,
		'sizeModifier':  wardrobe.sizeModifier,
		'gender': wardrobe.gender,
		'color': wardrobe.color,
		'pattern': wardrobe.pattern,
		'start_year': wardrobe.start_year,
		})

	if request.method == 'POST':
		
		form = WardrobeEditForm(request.POST) #validation
		form.wardrobeid = wardrobe.id
		if form.is_valid():
			wardrobe.name = form.cleaned_data['name']
			wardrobe.size = form.cleaned_data['size']
			wardrobe.sizeModifier = form.cleaned_data['sizeModifier']
			wardrobe.gender = form.cleaned_data['gender']
			wardrobe.color = form.cleaned_data['color']
			wardrobe.pattern = form.cleaned_data['pattern']
			wardrobe.start_year = form.cleaned_data['start_year']
			wardrobe.save()
			return HttpResponseRedirect('/homepage/wardrobe/')


	params['form'] = form

	return templater.render_to_response(request, 'wardrobe.edit.html', params)



class WardrobeEditForm(forms.Form):
	name = forms.CharField(required=True, max_length=100)
	size = forms.CharField(required=True, max_length=15)
	sizeModifier = forms.CharField(label ='Size modifier', required=True, max_length=100)
	gender = forms.CharField(required=True, max_length=1)
	color = forms.CharField()
	pattern = forms.CharField()
	start_year = forms.DateField()


	def clean_name(self):
		if len(self.cleaned_data['name']) <4:
			raise forms.ValidationError("Please a name greater than 4 characters.")
		wardrobe_count = hmod.Wardrobe_Item.objects.filter(name=self.cleaned_data['name']).exclude(id=self.wardrobeid).count()
		if wardrobe_count >=1:
			raise forms.ValidationError("This item already exists!")
		

		return self.cleaned_data['name']

@view_function
def create(request):
	'''creates a new user'''
	wardrobe = hmod.Wardrobe_Item()
	wardrobe.name = ''
	wardrobe.size =''
	wardrobe.sizeModifier = ''
	wardrobe.gender=''
	wardrobe.color = ''	
	wardrobe.pattern = ''	
	wardrobe.start_year = datetime.datetime.now()	
	wardrobe.save()

	return HttpResponseRedirect('/homepage/wardrobe.edit/{}'.format(wardrobe.id))



@view_function
def delete(request):
	params = {}
	try:
		wardrobe = hmod.Wardrobe_Item.objects.get(id=request.urlparams[0])
	except hmod.Wardrobe_Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/wardrobe/')

	hmod.Wardrobe_Item.objects.get(id=request.urlparams[0]).delete()

	return HttpResponseRedirect('/homepage/wardrobe/')