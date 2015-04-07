from django.db import models
from django.contrib.auth.models import User
#from polymorphic import PolymorphicModel
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
	###### INHERITED FIELDS #######
	# password
	# last_login
	#username = models.TextField()
	# first_name
	#last_name = models.TextField()
	#email = models.TextField()
	# is_staff
	# date_joined
	# USERNAME_FIELD
	# REQUIRED_FIELDS
	#user = models.OneToOneField(User)
	security_question=models.TextField()
	security_question_answer = models.TextField()
	street = models.TextField()
	city = models.TextField()
	state= models.TextField()
	pass_exp = models.DateField(null=True, blank=True)
	zip = models.IntegerField(null=True, blank=True)



class Wardrobe_Item(models.Model):
	size = models.TextField()
	name = models.TextField()
	sizeModifier = models.TextField()
	gender = models.CharField(max_length=1)
	color = models.TextField()
	pattern = models.TextField()
	start_year = models.DateField()

class Historical_Figure(models.Model):
	name = models.TextField()
	birth_date = models.DateField()
	birth_place = models.TextField()
	death_date = models.DateField()
	death_place = models.TextField()
	biographical_note = models.TextField()
	is_fictional = models.BooleanField(default=False)

class Order(models.Model):
	OrderNumber = models.IntegerField()
	orderDate = models.DateTimeField()
	Phone = models.TextField()
	datePacked = models.DateTimeField()
	datePaid = models.DateTimeField()
	dateShipped = models.DateTimeField()
	trackingNumber = models.TextField()
	#agent = models.ForeignKey(Agent)	

class Sale_Item(models.Model):
	name = models.TextField()
	description = models.TextField()
	low_price = models.DecimalField(max_digits=100, decimal_places=2, null=True)
	high_price = models.DecimalField(max_digits=100, decimal_places=2, null=True)
	price= models.DecimalField(max_digits=100, decimal_places=2)
	isRental = models.BooleanField(default=False)
	#area = models.ForeignKey(Area)

class Rentable_Item(Sale_Item):
	condition = models.TextField()
	newDamage = models.TextField()
	damageFee = models.TextField()
	lateFee = models.TextField()
	dueDate = models.DateField(null=True, blank=True)
	renterName = models.TextField(null=True, blank=True)
	renterEmail = models.TextField(null=True, blank=True)
	rentedDate = models.DateField(null=True, blank=True)


class Rental(models.Model):
  rentalTime = models.DateTimeField()
  dueDate = models.DateField()
  discountPercent = models.DecimalField(max_digits=4, decimal_places=2)
  fk = models.ForeignKey(Rentable_Item)
  customer = models.ForeignKey(User)
  cost = models.DecimalField(max_digits=10, decimal_places=2) #ADDED BY SCOTT 3/19/15


class Event(models.Model):
	name = models.TextField()
	description = models.TextField()
	startDate = models.DateField()
	endDate = models.DateField()
	isPublic = models.BooleanField(default=True)
	areas = models.TextField()
