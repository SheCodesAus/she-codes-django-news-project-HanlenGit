from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.utils import timezone


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = "__all__"
#         widgets = {
#             'pub_date': forms.DateInput(format=('%m/%d/%Y'),
# attrs={'class':'form-control', 'placeholder':'Select a date',
# 'type':'date'}),
# }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pub_date'].initial = timezone.now().strftime("%Y-%m-%dT%H:%M")
  
  