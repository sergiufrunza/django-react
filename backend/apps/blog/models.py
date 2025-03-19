from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models import F


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', symmetrical=False, blank=True, )
    likes_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def like(self, user):
        add = 1
        if not self.likes.filter(id=user.id).exists():
            self.likes.add(user)
        else:
            add = -1
            self.likes.remove(user)
        Blog.objects.filter(id=self.id).update(likes_count=F('likes_count') + add)
        return add

