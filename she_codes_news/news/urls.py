from django.urls import path
from . import views
from .views import StoryDeleteView, StoryEditView

app_name = 'news'

urlpatterns = [
    path('news/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('<int:pk>/delete', StoryDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', StoryEditView.as_view(), name='updateStory'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('category/<str:slug>/', views.CategoryView.as_view(), name='category'), 
]
