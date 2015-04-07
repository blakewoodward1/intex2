from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CHF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^.$', 'django_mako_plus.controller.router.route_request'),
    url(r'^.*$', 'django_mako_plus.controller.router.route_request' ),

    
)
