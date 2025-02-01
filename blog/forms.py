from django import forms
from .models import Post
from markdownx.fields import MarkdownxFormField

class PostForm(forms.ModelForm):
    text = MarkdownxFormField()
    
    class Meta:
        model = Post
        fields = ('title', 'text', 'post_Image')