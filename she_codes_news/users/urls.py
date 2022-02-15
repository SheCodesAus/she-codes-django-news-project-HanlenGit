from os import name
from django.urls import path
from .views import AuthorLoginView, CreateAccountView, UserProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),
    path('<int:pk>/', UserProfileView.as_view(),
name='user-profile'),
#     path('user/user-login-page'), AuthorLoginView.as_view(), 
# name= 'user-login-page',
]