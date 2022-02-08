from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('sign in')
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView): #django thing
    template_name = 'users/user-profile.html'
    context_object_name = 'author'
    model = CustomUser


