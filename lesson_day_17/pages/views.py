from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
    
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class InfoPageView(TemplateView):
    template_name = "info.html"
    

class LoginPageView(TemplateView):
    template_name = "accounts/login.html"