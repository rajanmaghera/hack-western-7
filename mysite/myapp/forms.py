from django import forms
from .models import *


class Post_Form(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_text', 'post_img']