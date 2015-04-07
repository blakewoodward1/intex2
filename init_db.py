#!/usr/bin/env python3
#INITIALIZE DJANGO
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'CHF.settings'
import django
import sys
django.setup()
from datetime import datetime
#REGULAR IMPORTS
import random, re
from django import forms
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess
import homepage.models as hmod
#DROP THE DATABASE
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])


#CREATE USERS
for data in [
	["Scott", "Hoopes", "hoopes@live.com", True, datetime.now(), "shoopes2", "xcountry9", "669 E", "Provo", "UT", "84606" ],
	["admin", "admin", "admin@live.com", True, datetime.now(), "admin", "admin", "669 E", "Provo", "UT", "84606" ],
	["Alyssa", "Bybee", "abybee4@gmail.com", False, datetime.now(), "ALB", "xcountry9", "2315 NE", "Provo", "UT", "84606" ],
	["Bridget", "Hoopes", "biddles234@live.com", False, datetime.now(), "BCH", "xcountry9", "2335 TIlden Way", "HEnderson", "NV", "84606" ],
	["Jessica", "Hoopes", "jjhpster@aol.com", False, datetime.now(), "JJH", "xcountry9", "Fipster", "ville", "NY", "84606" ],
	["Blake", "Woodward", "blakewoodward12@gmail.com", True, datetime.now(), "blakemw2", "password", "123 N", "Kaysville", "UT", "84037" ],

]:
	u = hmod.User()
	u.first_name = data[0]
	u.last_name = data[1]
	u.email = data[2]
	u.is_superuser = data[3]
	u.date_joined = data[4]
	u.username = data[5]
	u.set_password(data[6])
	u.street = data[7]
	u.city = data[8]
	u.state = data[9]
	u.zip = data[10]

	u.save()

#CREATE SALE_Item
for data in [
	["Musket", "This gun was used to kill dirty commie lobsterbacks", 250.99],
	["Wool Socks", "During the harsh winters, colonists wore socks like these", 12.93],
	["Covered Wagon", "Colonies built these to steal indian land.  Jerks.", 699.34],
	["Butter Churner", "The poor oppressed women had to churn butter all day while the lazy man-pigs sat around spitting thier chew", 87.22],
	["Muskrat trap", "Trappers sold pelts from muskrats caught in these traps", 12.05],
	["Leather Boots", "These were worn by the despicalbe 1% of the wealth holders who oppressed the poor and uneducated", 1999.00],
]:
	s = hmod.Sale_Item()
	s.name = data[0]
	s.description = data[1]
	s.price = data[2]
	s.save()

#CREATE Rentable_Item
for data in[
	["Pottery Wheel", "Used", "None", "1.00", "1.00 / day", "2015-03-06", "Make really pretty vases", "100.39"],
	["Anvil", "New", "None", "None", "$15.00 / day", "2015-03-06", "Have an enemy? no problem.", "315.12"],
	["Gillotuine", "New", "None", "None", "$150.00 / day", "2015-03-06", "France", "699.99"],
	["Colonial Outfit", "used", "None", "25.00", "$5.00 / day", "2015-03-06", "Made with original colonial design", "120.49"],
	["Modern Musket", "used", "None", "None", "15.00 / day", "2015-03-06", "User must go through background check and sign death waiver before being given the item", "1299.00"],
	["Horses", "New", "None", "None", "15.00 / day", "2015-03-06", "These new horses were just birthed and have no guarentee to survive", "528.44"],
]:
	r = hmod.Rentable_Item()
	r.name = data[0]
	r.condition = data[1]
	r.newDamage = data[2]
	r.damageFee = data[3]
	r.lateFee = data[4]
	r.dueDate = data[5]
	r.description = data[6]
	r.price = data[7]
	r.isRental = True
	r.save()

#CREATE Events
for data in [
	["George Washington Commemoration","Come and celebrate the birthday of our American Hero George Washington!","2015-04-12","2015-04-15",
	'''In the northwest field of the park there will be ticket booth to sign up for raffles. Near the restrooms is the picnic area where food is available for 
	purchase.  All areas will have sales available'''],
	["Murica Day","Come celebrate the day our glorious country rose from the dust.  Bring a cold can of beer and yer guns and yer fireworks!","2015-07-04","2015-07-04",'''In the northwest field of the park there will be ticket booth to sign up for raffles. Near the restrooms is the picnic area where food is available for 
	purchase.  All areas will have sales available'''],
	["Colonial Bakeoff","Sign up to bring your favorite colonial home made treat to be judged.","2015-08-12","2015-08-12",'''In the northwest field of the park there will be ticket booth to sign up for raffles. Near the restrooms is the picnic area where food is available for 
	purchase.  All areas will have sales available'''],
]:
	e = hmod.Event()
	e.name = data[0]
	e.description = data[1]
	e.startDate = data[2]
	e.endDate = data[3]
	e.isPublic = True
	e.areas= data[4]
	e.save()

#CREATE Retnals
# for data in [
# 	['2015-04-03 12:23:00-06', '2015-04-03', '0', 7, '1', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-01-12', '0', '8', '2', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-02-02', '0', '9', '3', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-03-12', '0', '10', '4', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-01-11', '0', '11', '1', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-02-11', '0', '12', '2', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-03-01', '0', '10', '5', '0.00'],
# 	['2015-04-03 12:23:00-06', '2015-04-11', '0', '9', '3', '0.00'],


# ]:
# 	e = hmod.Rental()
# 	e.rentalTime = data[0]
# 	e.dueDate = data[1]
# 	e.discountPercent = data[2]
# 	#e.fk = data[3]
# 	#e.customer = data[4]
# 	e.cost= data[5]
# 	e.save()
