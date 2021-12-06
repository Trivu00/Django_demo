from django.db.models import fields
from django.db.models.base import Model
from django.forms import forms
from usefulModels.models import Post
from django.views.generic.edit import CreateView
from django import forms
from .models import Comment

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.name_read = kwargs.pop('name_read',None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        post.author = self.author
        post.name_read = self.name_read
        post.save()
        
    class Meta:
        model = Post
        fields = ["note"]


class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()

    class Meta:
        model = Comment
        fields = ["body"]


