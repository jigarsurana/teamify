from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()

from api import views




#Person
urlpatterns = patterns('',
    
	url(r'^person/$' , views.person_create),
	
)

