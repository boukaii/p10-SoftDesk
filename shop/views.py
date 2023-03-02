from shop.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer, UserSerializer
from shop.models import Project, Contributor, Issue, Comment, User
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny


class UserSignUpView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)

    def get_queryset(self):
        projects_of_user = []
        is_author_or_contrib = Contributor.objects.filter(
            user=self.request.user).values()
        for user in is_author_or_contrib:
            projects_of_user.append(user['project_id'])
        return Project.objects.filter(id__in=projects_of_user)


class ContributorViewSet(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer

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

