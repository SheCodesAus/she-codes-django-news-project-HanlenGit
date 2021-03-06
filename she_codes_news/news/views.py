from re import template
from unicodedata import name
from django.views import generic
from django.urls import reverse_lazy
from .models import Category, NewsStory
from .forms import StoryForm
from django.views.generic.edit import DeleteView
from users.models import CustomUser
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:3]
        context['all_stories'] = NewsStory.objects.all()
        context['categories'] = Category.objects.all()
        
        return context

class CategoryView(generic.DetailView):
    model = Category
    slug_field = 'name'
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoryDeleteView(DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        if self.object.author != self.request.user:
            raise PermissionDenied()
        return super().form_valid(form)

class StoryEditView(UpdateView):
    model = NewsStory
    success_url = reverse_lazy('news:index')
    template = 'news/newsstory_confirm_edit.html'
    fields = "__all__"

    def form_valid(self, form):
        if self.object.author != self.request.user:
            raise PermissionDenied()
        return super().form_valid(form)




