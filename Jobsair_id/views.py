from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Blog
from .forms import PostForm


# Create your views here.
def index(request):
    # get 9 job post order by the newest published date
    posts = Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date').reverse()[:9]

    # get 3 blog post order by the highest view count
    blogs = Blog.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('views').reverse()[:3]
    return render(request, 'Jobsair_id/index.html', {'posts': posts,
                                                     'blogs': blogs})


def post_list(request):
    posts = Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date')
    return render(request, 'Jobsair_id/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Jobsair_id/post_detail.html', {'post': post})


def post_new(request):
    state = 'NEW JOB POST'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'Jobsair_id/post_edit.html', {'form': form, 'state': state})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    state = 'EDITING JOB POST'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail.html')
    else:
        form = PostForm(instance=post)
    return render(request, 'Jobsair_id/post_edit.html', {'form': form, 'post': post, 'state': state})


def about_us(request):
    return render(request, 'Jobsair_id/about-us.html', {})


def blog_list(request):
    blogs = Blog.objects.filter(
           published_date__lte=timezone.now()
           ).order_by('published_date').reverse()[:6]
    return render(request, 'Jobsair_id/blog.html', {'blogs': blogs})


def blog_detail(request, pk):
    view = Blog.objects.get(pk=pk)  # counting / tracking view
    view.views = view.views+1
    view.save()

    blog = get_object_or_404(Blog, pk=pk)  # error handling
    return render(request, 'Jobsair_id/blog-details.html', {'blog': blog,
                                                            'view': view})


def terms(request):
    return render(request, 'Jobsair_id/terms.html', {})


def login_user(request):
    return render(request, 'Jobsair_id/Login.html', {})


def register_user(request):
    return render(request, 'Jobsair_id/register.html', {})


def contact_us(request):
    return render(request, 'Jobsair_id/contact-us.html', {})
