from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='uncategorized')
    salary = models.BigIntegerField(blank=True, null=True)
    job_desc = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    comp_link = models.URLField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=100, default='Tag line unavailable')
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return self.title


class Member(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    desc = models.TextField()
    phone = models.BigIntegerField()
    company = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100, default='Jakarta')
    category = models.CharField(max_length=100, default='uncategorized')
    website = models.URLField(max_length=100, default='')

    def __str__(self):
        return str(self.user)
