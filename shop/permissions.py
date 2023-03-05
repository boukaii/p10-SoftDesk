from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Contributor, Project
from django.contrib.auth import get_user
from django.contrib.auth.models import AnonymousUser


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif obj.author == request.user:
            return True
        else:
            return False


class IsContributor(BasePermission):
    message = "Vous n'avez pas la permission d'effectuer cette action. " \
              "Vous ne faites pas partie des contributeurs du projet"

    def has_permission(self, request, view):
        if type(get_user(request)) is not AnonymousUser:
            if Contributor.objects.filter(project=view.kwargs['project_pk'],
                                          user=get_user(request)):
                return True
        else:
            return False


class IsLogged(BasePermission):
    message = 'Vous n\'avez pas la permission d\'effectuer cette action. ' \
              'Vous n\'êtes pas connecté.'

    def has_permission(self, request, view):
        user = get_user(request)
        if type(user) is AnonymousUser:
            return False
        else:
            return True


class ProjectAuthorOrContributorHimself(BasePermission):
    message = 'Vous n\'avez pas la permission d\'effectuer cette action. Vous ' \
              'n\'êtes pas l\'auteur du projet ou le contributeur concerné.'

    def has_permission(self, request, view):
        user = get_user(request)
        if request.method == 'DELETE':
            project = Project.objects.filter(id=view.kwargs['project_pk'])[0]
            contributor = Contributor.objects.filter(id=view.kwargs['pk'])[0]
            if project.author == user or user == contributor.user:
                return True
            else:
                return False
        else:
            return True
