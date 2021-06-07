from django.db import models


# Create your models here.

class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categoryes'


class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
