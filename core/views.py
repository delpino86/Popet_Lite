from django.views.generic.base import TemplateView



class HomePageView(TemplateView):

    template_name = "core/home.html"

class AboutView(TemplateView):

    template_name = "core/about.html"

class LoginView(TemplateView):

    template_name = "core/login.html"