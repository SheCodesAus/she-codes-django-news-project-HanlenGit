from django.contrib.auth import get_user_model
from django.db import models



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models. CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()

class ProjectProfile(models.Model):
    project_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name

# class Category(models.Model):
#     category = models.CharField(max_length=200, choices = 'categories')
#     choices = 'Program', 'Annoucenments'







     
