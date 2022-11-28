from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'type_of_post',
            'header',
            'text',
            'category',
            'user',
            'author'
        ]
