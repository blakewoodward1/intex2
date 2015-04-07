from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms


templater = get_renderer('homepage')


########################################################
###### Shows the list of sales
@view_function
def process_request(request):
	params = {}


	all_sale = hmod.Sale_Item.objects.all() #.filter, .exclude, .get
	params['all_sale'] = all_sale
	

	return templater.render_to_response(request, 'sale_item.html', params)


	########################################################
###### Edit a sale

@view_function
def edit(request):
	params = {}
	if request.user.is_authenticated():
		try:
			sale = hmod.Sale_Item.objects.get(id=request.urlparams[0])
		except hmod.Sale_Item.DoesNotExist:
			return HttpResponseRedirect('/homepage/sale_item/')
		

		form = SaleEditForm(initial={
			'name': sale.name,
			'description': sale.description,
			'low_price': sale.low_price,
			'high_price': sale.high_price,
			})

		if request.method == 'POST':
			form = SaleEditForm(request.POST) #validation
			form.saleid = sale.id
			if form.is_valid():
				sale.name = form.cleaned_data['name']
				sale.description = form.cleaned_data['description']
				sale.low_price = form.cleaned_data['low_price']
				sale.high_price= form.cleaned_data['high_price']
				sale.save()
				return HttpResponseRedirect('/homepage/sale_item/')


		params['form'] = form

		return templater.render_to_response(request, 'sale_item.edit.html', params)

	else:
		return HttpResponseRedirect('/homepage/anon_user')


class SaleEditForm(forms.Form):
	name = forms.CharField(required=True)
	description = forms.CharField( required=True)
	low_price = forms.DecimalField(required=True)
	high_price = forms.DecimalField()

	def clean_name(self):
		if len(self.cleaned_data['name']) <5:
			raise forms.ValidationError("Please include a name greater than 5 characters.")
		sale_count = hmod.Sale_Item.objects.filter(name=self.cleaned_data['name']).exclude(id=self.saleid).count()
		if sale_count >=1:
			raise forms.ValidationError("This item already exists in the database.")
		print(sale_count)

		return self.cleaned_data['name']


@view_function
def create(request):
	if request.user.is_authenticated():
		'''creates a new user'''
		sale = hmod.Sale_Item()
		sale.name = ''
		sale.description =''
		sale.high_price = '0'
		sale.low_price='0'
		sale.save()

		return HttpResponseRedirect('/homepage/sale_item.edit/{}'.format(sale.id))
	else:
		return HttpResponseRedirect('/homepage/anon_user')


@view_function
def delete(request):
	if request.user.is_authenticated():
		params = {}
		try:
			sale = hmod.Sale_Item.objects.get(id=request.urlparams[0])
		except hmod.Sale_Item.DoesNotExist:
			return HttpResponseRedirect('/homepage/sale_item/')

		hmod.Sale_Item.objects.get(id=request.urlparams[0]).delete()

		return HttpResponseRedirect('/homepage/sale_item/')
	else:
		return HttpResponseRedirect('/homepage/anon_user')