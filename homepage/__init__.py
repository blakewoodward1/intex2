# All apps that are DMP-enabled must have this setting in their app-level __init__.py
DJANGO_MAKO_PLUS = True
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import RedirectException
from django.dispatch import receiver
from homepage import models as hmod


###########################################
#### Create the templater for this app once
#templater == MakoTemplateRenderer('homepage')