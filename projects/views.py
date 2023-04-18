from projects.serializers import ProjectSerializer,\
    ContributorSerializer, IssueSerializer,\
    CommentSerializer, UserSerializer
from projects.models import Project, Contributor, Issue, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from projects.permissions import (
    ProjectPermissions,
    IssuePermissions,
    CommentPermissions,
)


class UserSignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ProjectPermissions]

    def get_queryset(self):
        contributors = Contributor.objects.filter(user=self.request.user)

        return (Project.objects.filter(contributor=self.request.user)
                | Project.objects.filter(contributor_project__in=contributors)).distinct()


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IssuePermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        project = self.kwargs['project_pk']
        return Issue.objects.filter(project_id=project)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CommentPermissions]

    def get_queryset(self):
        print(self.kwargs)
        project = self.kwargs['issue_pk']
        return Comment.objects.filter(issue_id=project)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(role=Contributor.CONTRIBUTOR)

    def get_queryset(self):
        project = self.kwargs['project_pk']
        return Contributor.objects.filter(project_id=project)
