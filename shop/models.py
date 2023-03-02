from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(unique=True)


class Project(models.Model):
    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    IOS = 'IOS'
    ANDROID = 'ANDROID'
    TYPES_CHOICES = (
        (BACKEND, 'Back-end'),
        (FRONTEND, 'Front-end'),
        (IOS, 'iOS'),
        (ANDROID, 'Android')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=30)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='projects')

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='contributors')
    project = models.ForeignKey('Project',
                                on_delete=models.CASCADE,
                                related_name='contributors')


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


