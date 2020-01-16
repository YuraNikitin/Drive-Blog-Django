from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{},{}'.format(self.title, self.slug)

    class Meta():
        ordering = ['title']
