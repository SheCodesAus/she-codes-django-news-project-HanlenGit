from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory

# Create your views here.

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('sign in')
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView): #django thing
    template_name = 'users/user-profile.html'
    context_object_name = 'author'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context

class AuthorLoginView(generic.DetailView):
    template_name = 'user/user-login-page'
    model = CustomUser
    context_object_name = 'user'

