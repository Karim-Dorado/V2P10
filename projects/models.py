from django.db import models
from django.conf import settings


TYPE = [
    ('back', 'Back-end'),
    ('front', 'Front-end'),
    ('ios', 'IOS'),
    ('android', 'Android')
    ]


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255, blank=True)
    type = models.CharField(choices=TYPE, max_length=7)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='author'
                               )