from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'salary', 'job_desc', 'address',
                  'comp_link',)
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}), 
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   'salary': forms.NumberInput(attrs={'class': 'form-control'}), 
                   'job_desc': forms.Textarea(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}),
                   'comp_link': forms.URLInput(attrs={'class': 'form-control'}),}
