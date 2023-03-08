from shop.serializers import ProjectSerializer,\
    ContributorSerializer, IssueSerializer,\
    CommentSerializer, UserSerializer
from shop.models import Project, Contributor, Issue, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


class UserSignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retourne la liste de tout les
         contributeurs d'un projet avec son ID
        """
        project = self.kwargs['project_id']
        return Contributor.objects.filter(project=project)

    def perform_create(self, serializer):
        """Créer un contributeur sur un projet
         terminé grace a son ID

        """
        project = self.kwargs['project_id']
        project = Project.objects.get(id=project)
        serializer.save(project=project)


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        project = self.kwargs['project_id']
        project = Project.objects.get(id=project)
        serializer.save(author_user=self.request.user, project=project)

    def get_queryset(self):
        """Retourne la liste de tout les
         problèmes d'un projet avec son ID
        """
        project = self.kwargs['project_id']
        return Issue.objects.filter(project=project)


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        issue = self.kwargs['issue_id']
        issue = Issue.objects.get(id=issue)
        serializer.save(author_user=self.request.user, issue=issue)

    def get_queryset(self):
        """
        On récupère tout les commentaires dans une liste
        """
        issue = self.kwargs['issue_id']
        return Comment.objects.filter(issue=issue)


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        contributors = Contributor.objects.filter(user=self.request.user)

        return (Project.objects.filter(contributor=self.request.user))
                # | Project.objects.filter(project_created_by__in=contributors)).distinct()




























#
#
# class ProjectViewSet(viewsets.ModelViewSet):
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         """L'auteur est automatiquement enregistré
#          en tant qu'utilisateur authentifié
#          """
#         serializer.save(author_user=self.request.user)
#
#     def get_queryset(self):
#         """Cette vue ne doit renvoyer que les projets si l'utilisateur authentifié est le
#         auteur ou l'un des contributeurs.
#         """
#         projects_of_user = []
#         is_author_or_contrib = Contributor.objects.filter(
#             user=self.request.user).values()
#         for user in is_author_or_contrib:
#             projects_of_user.append(user['project_id'])
#         return Project.objects.filter(id__in=projects_of_user)
