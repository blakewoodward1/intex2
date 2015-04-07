from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
import homepage.models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.db.models import Max
import datetime

templater = get_renderer('homepage')


########################################################
###### Shows the list of orders
@view_function
def process_request(request):
	params = {}
	if request.user.is_authenticated():

		all_order = hmod.Order.objects.all().order_by('OrderNumber').reverse() #.filter, .exclude, .get
		params['all_order'] = all_order
		

		return templater.render_to_response(request, 'order.html', params)

	else:
		return HttpResponseRedirect('/login/?next=%s' % request.path)
		#return HttpResponseRedirect('/homepage/anon_user/')

	########################################################
###### Edit an order

@view_function
def edit(request):
	params = {}
	if request.user.is_authenticated():

		try:
			order = hmod.Order.objects.get(id=request.urlparams[0])
		except hmod.Order.DoesNotExist:
			return HttpResponseRedirect('/homepage/order/')
		

		form = OrderEditForm(initial={
			'OrderNumber': order.OrderNumber,
			'orderDate': order.orderDate,
			'Phone': order.Phone,
			'datePacked': order.datePacked,
			'datePaid': order.datePaid,
			'dateShipped': order.dateShipped,
			'trackingNumber': order.trackingNumber,
			
			})

		if request.method == 'POST':
			form = OrderEditForm(request.POST) #validation
			form.OrderNumber = order.OrderNumber
			if form.is_valid():
				order.OrderNumber = form.cleaned_data['OrderNumber']
				order.orderDate = form.cleaned_data['orderDate']
				order.Phone = form.cleaned_data['Phone']
				order.datePacked= form.cleaned_data['datePacked']
				order.datePaid= form.cleaned_data['datePaid']
				order.dateShipped = form.cleaned_data['dateShipped']
				order.trackingNumber =form.cleaned_data['trackingNumber']
				order.save()
				return HttpResponseRedirect('/homepage/order/')


		params['form'] = form

		return templater.render_to_response(request, 'order.edit.html', params)
	else:
		return HttpResponseRedirect('/homepage/anon_user')


class OrderEditForm(forms.Form):
	OrderNumber = forms.IntegerField(required=True)
	orderDate = forms.DateField( required=True)
	Phone = forms.CharField(required=True, max_length=20)
	datePacked = forms.DateField()
	datePaid = forms.DateField()
	dateShipped = forms.DateField()
	trackingNumber = forms.CharField(required=True)
	
	def clean_OrderNumber(self):
		order_count = hmod.Order.objects.filter(OrderNumber=self.cleaned_data['OrderNumber']).exclude(OrderNumber=self.OrderNumber).count()
		if order_count >=1:
			raise forms.ValidationError("There is already an order with that number.")
		return self.cleaned_data['OrderNumber']


@view_function
def create(request):
	if request.user.is_authenticated():

		'''creates a new user'''
		order = hmod.Order()
		
		order_max = hmod.Order.objects.all().aggregate(Max('OrderNumber'))

		order.OrderNumber = order_max['OrderNumber__max']+1
		order.orderDate =datetime.datetime.now()
		order.Phone = ''
		order.datePacked=datetime.datetime.now()
		order.datePaid= datetime.datetime.now()
		order.dateShipped = datetime.datetime.now()
		order.trackingNumber = ''
		order.save()

		return HttpResponseRedirect('/homepage/order.edit/{}'.format(order.id))
	else:
		return HttpResponseRedirect('homepage/anon_user')

@view_function
def delete(request):
	params = {}
	if request.user.is_authenticated():
		try:
			order = hmod.Order.objects.get(id=request.urlparams[0])
		except hmod.Order.DoesNotExist:
			return HttpResponseRedirect('/homepage/order/')

		hmod.Order.objects.get(id=request.urlparams[0]).delete()

		return HttpResponseRedirect('/homepage/order/')
	else:
		return HttpResponseRedirect('homepage/anon_user')