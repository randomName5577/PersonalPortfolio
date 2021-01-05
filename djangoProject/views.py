from django.views.generic import TemplateView, ListView
from projects.models import Project
from blog.models import Post
from itertools import chain
# class HomePage(TemplateView):
#     template_name = 'index.html'

class SearchView(ListView):
    model = Project
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresults = Project.objects.filter(title__contains=query)
            blogresults = Post.objects.filter(title__contains=query)
            result = list(chain(postresults,blogresults))
        else:
            result =None
        return result

