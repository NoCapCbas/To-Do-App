# created by me, form representation of our model
# imports form
from django import forms
from django.forms import ModelForm
# imports all models
from .models import *
# creates a form using our model
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    #must give this class minimum two variables
    class Meta:
        # name of our model
        model = Task
        # what fields from our model do we want to use
        fields = '__all__'
