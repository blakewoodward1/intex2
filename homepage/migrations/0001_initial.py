# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=30, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('security_question', models.TextField()),
                ('security_question_answer', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('pass_exp', models.DateField(null=True, blank=True)),
                ('zip', models.IntegerField(null=True, blank=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', to='auth.Group', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', to='auth.Permission', related_name='user_set', related_query_name='user')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('isPublic', models.BooleanField(default=True)),
                ('areas', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Historical_Figure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('birth_date', models.DateField()),
                ('birth_place', models.TextField()),
                ('death_date', models.DateField()),
                ('death_place', models.TextField()),
                ('biographical_note', models.TextField()),
                ('is_fictional', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('OrderNumber', models.IntegerField()),
                ('orderDate', models.DateTimeField()),
                ('Phone', models.TextField()),
                ('datePacked', models.DateTimeField()),
                ('datePaid', models.DateTimeField()),
                ('dateShipped', models.DateTimeField()),
                ('trackingNumber', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('rentalTime', models.DateTimeField()),
                ('dueDate', models.DateField()),
                ('discountPercent', models.DecimalField(max_digits=4, decimal_places=2)),
                ('cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('customer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('low_price', models.DecimalField(null=True, max_digits=100, decimal_places=2)),
                ('high_price', models.DecimalField(null=True, max_digits=100, decimal_places=2)),
                ('price', models.DecimalField(max_digits=100, decimal_places=2)),
                ('isRental', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rentable_Item',
            fields=[
                ('sale_item_ptr', models.OneToOneField(to='homepage.Sale_Item', auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('condition', models.TextField()),
                ('newDamage', models.TextField()),
                ('damageFee', models.TextField()),
                ('lateFee', models.TextField()),
                ('dueDate', models.DateField(null=True, blank=True)),
                ('renterName', models.TextField(null=True, blank=True)),
                ('renterEmail', models.TextField(null=True, blank=True)),
                ('rentedDate', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=('homepage.sale_item',),
        ),
        migrations.CreateModel(
            name='Wardrobe_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('size', models.TextField()),
                ('name', models.TextField()),
                ('sizeModifier', models.TextField()),
                ('gender', models.CharField(max_length=1)),
                ('color', models.TextField()),
                ('pattern', models.TextField()),
                ('start_year', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rental',
            name='fk',
            field=models.ForeignKey(to='homepage.Rentable_Item'),
            preserve_default=True,
        ),
    ]
