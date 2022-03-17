from django.db import models
from projects.models import Project
from django.conf import settings

ROLE = [
    ('admin', 'Admin'),
    ('po', 'PO'),
    ('dev', 'Developer'),
    ]

PERMISSION = (
    ('author', 'Author'),
    ('contributor', 'Contributor'),
)

class Contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='user_contributor')
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='project_contributor')
    permission = models.CharField(choices=PERMISSION, max_length=128)
    role = models.CharField(choices=ROLE, max_length=128)

    def __str__(self):
        return f'{self.user}'