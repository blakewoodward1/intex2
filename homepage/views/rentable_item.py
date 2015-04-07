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
	if request.user.is_authenticated():


		all_item = hmod.Rentable_Item.objects.all() #.filter, .exclude, .get
		params['all_item'] = all_item
		

		return templater.render_to_response(request, 'rentable_item.html', params)
	else:
		return HttpResponseRedirect('/homepage/anon_user/')

	########################################################
###### Edit a Wardrobe

@view_function
def edit(request):
	if request.user.is_authenticated():
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
				item.name = form.cleaned_data['name']
				item.condition = form.cleaned_data['condition']
				item.newDamage = form.cleaned_data['newDamage']
				item.damageFee= form.cleaned_data['damageFee']
				item.lateFee= form.cleaned_data['lateFee']
				item.save()
				return HttpResponseRedirect('/homepage/rentable_item/')


		params['form'] = form

		return templater.render_to_response(request, 'rentable_item.edit.html', params)
	else:
		HttpResponseRedirect("/homepage/anon_user")


class ItemEditForm(forms.Form):
	name = forms.CharField(required=True, max_length=100)
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
		return self.cleaned_data['name']


@view_function
def create(request):
	'''creates a new user'''
	if request.user.is_authenticated():

		item = hmod.Rentable_Item()
		item.name = ''
		item.condition =""
		item.newDamage = ''
		item.damageFee=""
		item.lateFee=""
		item.save()

		return HttpResponseRedirect('/homepage/rentable_item.edit/{}'.format(item.id))
	else:
		return HttpResponseRedirect("/homepage/anon_user")

@view_function
def delete(request):
	params = {}
	if request.user.is_authenticated():

		try:
			item = hmod.Rentable_Item.objects.get(id=request.urlparams[0])
		except hmod.Rentable_Item.DoesNotExist:
			return HttpResponseRedirect('/homepage/rentable_item/')

		hmod.Rentable_Item.objects.get(id=request.urlparams[0]).delete()

		return HttpResponseRedirect('/homepage/rentable_item/')
	else:
		return HttpResponseRedirect("/homepage/anon_user")


@view_function
def query(request):
	params = {} 

	params['all_item'] = hmod.Rentable_Item.objects.raw('SELECT * from homepage_Rentable_Item WHERE "dueDate" < NOW()')

	return templater.render_to_response(request, 'rentable_item.html', params) 



@view_function
def query_thirty(request):
	params = {}

	today = datetime.date.today()
	thirty_days_ago = today - datetime.timedelta(days=30)
	sixty_days_ago = today - datetime.timedelta(days=59)
	#params['Rentable_Item'] = hmod.Rentable_Item.objects.filter(dueDate__gte=today1, dueDate__lte=thirty_days_ago1)

	params['all_item'] = hmod.Rentable_Item.objects.filter(dueDate__range=(sixty_days_ago, thirty_days_ago))

	return templater.render_to_response(request, 'rentable_item.html', params)

@view_function
def query_sixty(request):
	params = {}
	
	today = datetime.date.today()
	thirty_days_ago = today - datetime.timedelta(days=30)
	sixty_days_ago = today - datetime.timedelta(days=60)
	ninety_days_ago = today - datetime.timedelta(days=90)

	params['all_item'] = hmod.Rentable_Item.objects.filter(dueDate__range=(ninety_days_ago, sixty_days_ago))

	return templater.render_to_response(request, 'rentable_item.html', params)

@view_function
def query_ninety(request):
	params = {}
	
	today = datetime.date.today()
	sixty_days_ago = today - datetime.timedelta(days=60)
	ninety_days_ago = today - datetime.timedelta(days=90)
	params['all_item'] = hmod.Rentable_Item.objects.filter(dueDate__lte=ninety_days_ago)

	return templater.render_to_response(request, 'rentable_item.html', params)




@view_function
def send_email(request):
	params = {}

	dates = []
	dates.append(30)
	dates.append(60)
	dates.append(90)

	print(">>>>>>>>>>>>>>>>BEGINNING FOR LOOP")
	for date in dates:
		today = datetime.date.today()
		print(">>>>>>>>>>>>>>>>Got today")
		days_ago = today - datetime.timedelta(days=date)
		print(">>>>>>>>>>>>>>>>Set days ago")
		day_range =29
		if date == 90:
			day_range=10000
		print(">>>>>>>>>>>>>>>>Determined date range")

		ODItems = hmod.Rentable_Item.objects.filter(dueDate__range=(days_ago - datetime.timedelta(days=day_range), days_ago))
		print(">>>>>>>>>>>>>>>>got overdue items for range", days_ago, days_ago-datetime.timedelta(days=day_range))
		print(">>>>>>>>>>>>>>>>Overdue items are: ", ODItems)
		print(">>>>>>>>>>>>>>>>Beginning email loop")
		for odItem in ODItems:
			html_cont = get_template('email_overdue.html')
			d = Context({'first_name': odItem.renterName, 'item_name': odItem.name, 'days_overdue': today - odItem.dueDate  })
			print(">>>>>>>>>>>>>>>>Context Set")

			msg = EmailMultiAlternatives(
			'Overdue Rental Alert',
		    'Content goes here.',
		    'chf2-14@outlook.com',
		    [odItem.renterEmail]
		    )
			print(">>>>>>>>>>>>>>>>Rendering Message")

			html_content = html_cont.render(d)
			print(">>>>>>>>>>>>>>>>Message Rendered")

			msg.attach_alternative(html_content, "text/html")
			#msg.attach_alternative(get_template('email_forgot.html').render(Context()), "text/html")
			msg.send()
			print(">>>>>>>>>>>>>>>>Message sent")

	params['all_item'] = hmod.Rentable_Item.objects.all() #.filter, .exclude, .get
	return templater.render_to_response(request, 'rentable_item.html', params)
