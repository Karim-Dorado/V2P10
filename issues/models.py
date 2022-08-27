from django.db import models
from django.conf import settings
from projects.models import Project
from users.models import User

PRIORITY = [
    ('l', 'Low'),
    ('m', 'Medium'),
    ('h', 'High'),
    ]

TAG = [
    ('b', 'Bug'),
    ('f', 'Amélioration'),
    ('i', 'Tâche')
    ]

STATUT = [
    ('td', 'To do'),
    ('ip', 'In progress'),
    ('d', 'Done')
    ]


class Issue(models.Model):
    """
    Model that represents an issue.
    """
    title = models.CharField(max_length=128, blank=False)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=12, choices=TAG)
    priority = models.CharField(max_length=7, choices=PRIORITY)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='issue_related'
                                )
    status = models.CharField(max_length=8, choices=STATUT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.RESTRICT,
                               related_name='issue_created_by'
                               )
    assignee = models.ForeignKey(User,
                                 on_delete=models.RESTRICT,
                                 related_name='issue_assigned_to',
                                 )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
