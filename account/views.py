from django.shortcuts import render

# Create your views here.

class LoginView(SuccessURLAllowedHostsMixin,FormView):

    form_class = AuthentificationForm
    authentification_form = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'

from django.views.generic import TemplateView

class Dashboardview(TemplateView):
	template_name = 'account/Dashboard.html'
		