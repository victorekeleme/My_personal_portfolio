from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, DetailView
from portfolioApp.models import Project, Skill
from portfolioApp.forms import EmailForm
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST

# Create your views here.

#
# class ProfileListView(TemplateView):
#
#     template_name ='portfolioApp/base.html'

class ProfileListView(ListView):
    model = Project
    context_object_name = 'project'
    template_name = 'portfolioApp/base.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        skill = Skill.objects.all()
        context['skills'] = skill
        context['email_form'] = EmailForm()
        return context

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = EMAIL_HOST



