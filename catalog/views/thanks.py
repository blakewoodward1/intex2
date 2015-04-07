from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import random
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod

from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import hashlib



templater = get_renderer('catalog')

@view_function
def process_request(request):
	params ={}
	print(">>>>>>>>>asdf>>>>>>>>>>>>> looking for all items", request.session['shopping_cart'])
	all_items = hmod.Sale_Item.objects.all()
	cart_items=[]
	print(">>>>>>>>>>>>>>>>>> Found Items")
	cart_items=request.session['shopping_cart']#.keys()
	params['cart']=request.session['shopping_cart']
	params['all_items'] = all_items
	print(">>>>>>>>>>>>>>>>>>LOoking for User")
	user = hmod.User.objects.get(username=request.user)
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>Found user")

	params['user']= user

	html_cont = get_template('email_receipt.html')

	emailbody = templater.render(request, 'email_receipt.html', params)    

	send_mail("Order Receipt", emailbody, 'chf2-14@outlook.com', ['hoopes@live.com'], html_message=emailbody, fail_silently=False)




	# print(">>>>>>>>>>>>>>>>>>>>Preparing message context dictionary")

	# d = Context({'id': user.id,  'first_name': user.first_name, 'cart':params['cart'], 'items':params['all_items'] })

	# print(">>>>>>>>>>>>>>>>>>>>Preparing Email")

	# msg = EmailMultiAlternatives(
 #    'Order Receipt',
	# 'Content goes here.',
	# 'chf2-14@outlook.com',
	# [user.email]
	# )
	# print(">>>>>>>>>>>>>>>>>>>>Preparing html message from d")

	# html_content = html_cont.render(d)

	# msg.attach_alternative(html_content, "text/html")
	# print(">>>>>>>>>>>>>>>>>>>>sending")

	# msg.send()


	
	return templater.render_to_response(request, 'thanks.html', params)
