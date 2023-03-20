from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    cover_img = models.ImageField(upload_to='images/')
    content = models.TextField()
    author_name = models.CharField(max_length=255)
    author_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
