from django.conf.urls import url
from . import views

url(r'^$', 'main.views.index', name='home'),

