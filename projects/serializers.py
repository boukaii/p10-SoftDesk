from projects.models import Contributor, Issue, Project, Comment
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "role"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project",
            "author_id",
            "assignee_user",
            "created_time",
        ]


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'contributor']

    def validate_title(self, value):
        if Project.objects.filter(title=value).exists():
            raise ValidationError({'title error': 'Ce titre de project existe déjà'})
        return value


class ProjectDetailSerializer(ModelSerializer):
    contributor_project = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'contributor_project']

    def validate_title(self, value):
        if Project.objects.filter(title=value).exists():
            raise ValidationError({'title error': 'Ce titre de project existe déjà'})
        return value


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "created_time", "description", "author", "issue"]
