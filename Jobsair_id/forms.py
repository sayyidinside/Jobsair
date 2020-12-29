from django import forms
from .models import Post, Blog, Category


# Dynamic category
category_list = []
categories = Category.objects.all().values_list('name', 'name').order_by('name')
for category in categories:
    category_list.append(category)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'salary', 'job_desc', 'address',
                  'comp_link',)
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'category': forms.Select(choices=category_list, attrs={'class': 'form-control'}),
                   'salary': forms.NumberInput(attrs={'class': 'form-control'}),
                   'job_desc': forms.Textarea(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}),
                   'comp_link': forms.URLInput(attrs={'class': 'form-control'}), }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('author', 'title', 'tag_line', 'content', )
        widgets = {'author': forms.TextInput(attrs={'class': 'form-control'}),
                   'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'tag_line': forms.TextInput(attrs={'class': 'form-control'}),
                   'content': forms.Textarea(attrs={'class': 'form-control'}), }
