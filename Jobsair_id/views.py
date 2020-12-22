from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date').reverse()[:9]
    return render(request, 'Jobsair_id/index.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date')
    return render(request, 'Jobsair_id/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Jobsair_id/post_detail.html', {'post': post})


def about_us(request):
    return render(request, 'Jobsair_id/about-us.html', {})


def terms(request):
    return render(request, 'Jobsair_id/terms.html', {})


def login_user(request):
    return render(request, 'Jobsair_id/Login.html', {})


def register_user(request):
    return render(request, 'Jobsair_id/register.html', {})
