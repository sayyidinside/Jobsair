from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'salary', 'job_desc', 'address',
                  'comp_link',)
