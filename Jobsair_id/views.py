from django.contrib import messages
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Blog, Category
from .forms import PostForm, BlogForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.cache import cache


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
    return render(request,
                  'Jobsair_id/index.html',
                  {'posts': posts, 'blogs': blogs})


def post_list(request):
    posts = Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date').reverse()
    paginator = Paginator(posts, 12)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request,
                  'Jobsair_id/post_list.html',
                  {'page': page})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,
                  'Jobsair_id/post_detail.html',
                  {'post': post})


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
        return render(request,
                      'Jobsair_id/post_edit.html',
                      {'form': form, 'state': state})


@login_required(login_url='login')
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
            return redirect('post_detail',  pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,
                  'Jobsair_id/post_edit.html',
                  {'form': form, 'post': post, 'state': state})


def about_us(request):
    return render(request,
                  'Jobsair_id/about-us.html',
                  {})


def blog_list(request):
    blogs = Blog.objects.filter(
           published_date__lte=timezone.now()
           ).order_by('published_date').reverse()[:6]
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request,
                  'Jobsair_id/blog.html',
                  {'page': page})


def blog_detail(request, pk):
    view = Blog.objects.get(pk=pk)  # counting / tracking view
    view.views = view.views+1
    view.save()

    blog = get_object_or_404(Blog, pk=pk)  # error handling
    return render(request,
                  'Jobsair_id/blog-details.html',
                  {'blog': blog,
                   'view': view})


def blog_new(request):
    state = 'NEW BLOG POST'
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
        return render(request,
                      'Jobsair_id/blog_edit.html',
                      {'form': form, 'state': state})


@login_required(login_url='login')
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    state = 'EDITING JOB POST'
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.published_date = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
        return render(request,
                      'Jobsair_id/blog_edit.html',
                      {'form': form, 'blog': blog, 'state': state})


def terms(request):
    return render(request, 'Jobsair_id/terms.html', {})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or Password is incorrect')
        return render(request, 'Jobsair_id/Login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,
                                 'Account ' + user + ' has been created successfully')
                return redirect('login')
            else:
                messages.error(request, form.errors)
        form = RegisterForm()
        return render(request,
                      'Jobsair_id/register.html',
                      {'form': form})


def contact_us(request):
    return render(request,
                  'Jobsair_id/contact-us.html',
                  {})


def job_category(request, cats):
    categories = Post.objects.filter(category=cats).order_by('published_date').reverse()
    paginator = Paginator(categories, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request,
                  'Jobsair_id/post_category.html',
                  {'cats': cats, 'page': page})


def post_search(request):
    posts = Post.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date')
    search = request.GET.get('data')
    if search is not None:
        if search != '' and search is not None:
            cache.set('search', search)
            posts = posts.filter(
                    Q(title__icontains=search) |
                    Q(company__icontains=search) |
                    Q(category__icontains=search)).distinct()
    else:
        search = cache.get('search')
        posts = posts.filter(
                    Q(title__icontains=search) |
                    Q(company__icontains=search) |
                    Q(category__icontains=search)).distinct()

    print(search)
    print(posts)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request, 'Jobsair_id/post_search.html', {'search': search, 'page': page})


def blog_search(request):
    blogs = Blog.objects.filter(
            published_date__lte=timezone.now()
            ).order_by('published_date').reverse()
    search = request.GET.get('data')
    if search is not None:
        if search != '' and search is not None:
            cache.set('search', search)
            blogs = blogs.filter(
                    Q(title__icontains=search) |
                    Q(author__icontains=search) |
                    Q(tag_line__icontains=search)).distinct()
    else:
        search = cache.get('search')
        blogs = blogs.filter(
                    Q(title__icontains=search) |
                    Q(author__icontains=search) |
                    Q(tag_line__icontains=search)).distinct()

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    return render(request, 'Jobsair_id/blog_search.html', {'search': search, 'page': page})
