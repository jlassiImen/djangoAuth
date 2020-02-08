from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account.views import profile as views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^dashboard/$', views, name='dashboard'),
    url(r'^logout/$', auth_views.login, {'template_name': 'account/login.html'}, name='logout'),
]