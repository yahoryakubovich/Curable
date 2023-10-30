from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class ArticlesPageView(TemplateView):
    template_name = 'articles.html'

class ForumPageView(TemplateView):
    template_name = 'forum.html'

class PsychologistPageView(TemplateView):
    template_name = 'psychologist.html'
