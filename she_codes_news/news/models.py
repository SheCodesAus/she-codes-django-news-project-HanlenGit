from unicodedata import category
from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True)
    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models. CASCADE
    )
    pub_date = models.DateTimeField()
    
    content = models.TextField()
    image = models.URLField(null=True, blank=True)

    category = models.ForeignKey(
        Category,
        blank=True, null=True, 
        on_delete=models.SET_NULL, 
        related_name="stories"
    )

    class Meta:
        ordering = ['-pub_date']

    # categories = (
    #     ('NEWS', 'News'),
    #     ('PROGRAM', 'Program'),
    #     ('ANNOUNCEMENTS', 'Announcements'),
    #     ('CAREERS', 'Careers'),
    # )

    # category = models.CharField(max_length=200, choices = categories, default='news')


class ProjectProfile(models.Model):
    project_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name











     
