from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    linkedin = models.URLField()
    github = models.URLField()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)
