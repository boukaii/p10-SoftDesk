from django.conf import settings
from django.db import models


class Project(models.Model):
    PROJECT_TYPES = [
                    ('BE', 'Back-end'),
                    ('FE', 'Front-end'),
                    ('IOS', 'IOS'),
                    ('ANDROID', 'Android'),
                    ]

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=PROJECT_TYPES)
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT,
                                    related_name='project_created_by')

    def __str__(self):
        return self.title


class Contributor(models.Model):
    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    CHOICES = [
        (AUTHOR, 'Auteur'),
        (CONTRIBUTOR, 'Contributeur'),
    ]
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True, related_name='contributor_project')
    role = models.CharField(max_length=30, choices=CHOICES, verbose_name='role')


class Issue(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='issues_auteur')
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='issues_assigne')
    priority = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project',
                                on_delete=models.CASCADE,
                                related_name='issues')

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='comments')
    issue = models.ForeignKey('Issue',
                              on_delete=models.CASCADE,
                              related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
