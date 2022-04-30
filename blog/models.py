from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Yazi(models.Model):
    title = models.CharField(max_length=200)   
    image = models.ImageField(upload_to="blog_images")
    description = RichTextField()
    slug = models.SlugField(unique=True, blank=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)