from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=450)
    description = models.TextField(null=True, blank=True)
    post = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("id",)
