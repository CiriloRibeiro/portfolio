from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    created_at = models.DateField(auto_now_add=True)
    headline = models.TextField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    project_link = models.URLField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.headline
