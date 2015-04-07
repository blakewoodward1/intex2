from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
import datetime

from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django import forms


templater = get_renderer('homepage')


########################################################
###### Shows the list of wardrobe
@view_function
def process_request(request):
	params = {}

	all_item = hmod.Rentable_Item.objects.raw('SELECT * from homepage_Rentable_Item WHERE "rentedDate" <= NOW()')
	params['all_item'] = all_item
		

	return templater.render_to_response(request, 'rental_return.html', params)


	########################################################
###### Edit a Wardrobe

@view_function
def RReturn(request):
	params = {}

	try:
		item = hmod.Rentable_Item.objects.get(id=request.urlparams[0])
	except hmod.Rentable_Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/rentable_item/')
	

	form = ItemEditForm(initial={
		'name': item.name,
		'condition':  item.condition,
		'newDamage': item.newDamage,
		'damageFee': item.damageFee,
		'lateFee': item.lateFee,
		})

	if request.method == 'POST':
		form = ItemEditForm(request.POST) #validation
		form.rentable_itemid = item.id
		if form.is_valid():
			item.condition = form.cleaned_data['condition']
			item.newDamage = form.cleaned_data['newDamage']
			item.damageFee= form.cleaned_data['damageFee']
			print(item.damageFee)
			item.lateFee= form.cleaned_data['lateFee']
			item.rentedDate=None
			item.save()
			print(">>>>>>>>>>>>>>GEtting fee")
			if int(form.cleaned_data['damageFee']) > 0:

				params['fee']= int(form.cleaned_data['damageFee'])
				
				fee = int(form.cleaned_data['damageFee'])
				print(">>>>>>>>>>>>>>>", fee)
				return HttpResponseRedirect('/homepage/payment/' + str(fee))

		
		return HttpResponseRedirect('/homepage/rental_return.html/')


	params['form'] = form

	return templater.render_to_response(request, 'rentable_item.edit.html', params)


class ItemEditForm(forms.Form):
	condition = forms.CharField(required=True)
	newDamage = forms.CharField(label='New Damage', required=True)
	damageFee = forms.CharField(label='Damage Fee')
	lateFee = forms.CharField(label='Late Fee')
	

	def clean_name(self):
		if len(self.cleaned_data['name']) <5:
			raise forms.ValidationError("Please a name greater than 5 characters.")
			item_count = hmod.Rentable_Item.objects.filter(name=self.cleaned_data['name']).exclude(id=self.rentable_itemid).count()
			if item_count >=1:
				raise forms.ValidationError("This item already exists in the databases")
		return self.cleaned_data

