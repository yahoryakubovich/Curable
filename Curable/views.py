from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'