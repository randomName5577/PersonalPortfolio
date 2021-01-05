from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContactForm
from .models import ContactMe

from projects.models import Project
from blog.models import Post


class HomePage(TemplateView):
    template_name = 'index.html'
    page_title = 'Coding with Jayson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(title__contains = 'discord bot')
        context['blogs'] = Post.objects.filter(title__contains='gaming on windows 10')

        return context

class AboutMePage(TemplateView):
    template_name = 'aboutme.html'
    title = 'About Me'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = {'Python': 'five', 'Django': 'four', 'Linux': 'four', 'SQL': 'four', 'C#': 'three',
                             'SolidWorks': 'three', 'Matlab': 'three', 'PowerApps': 'three', 'Data Visualization': 'five',
                             'Automation': 'five', 'Web Scraping': 'five', 'Machine Learning': 'four'}

        return context

def contactmepage(request):
    form = ContactForm()
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactMe(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                body=form.cleaned_data['body'],
            )
            contact.save()
            submitted =True
        else:
            print(form.errors)

    context = {
        'form': form,
        'submitted' : submitted
    }
    return render(request, 'contactme.html', context=context)
