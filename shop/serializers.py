from rest_framework.serializers import ModelSerializer
from shop.models import Contributor, Issue, Project, Comment
from rest_framework import serializers
from shop.models import User


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

        return


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author_user_id",
        ]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user_id", "project_id"]


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
            "project_id",
            "author_user_id",
            "assignee_user",
            "created_time",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "created_time", "description", "author_user_id", "issue_id"]













































# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id',
#                   'username',
#                   'first_name',
#                   'last_name',
#                   'email',
#                   'password']
#
#     # create_user to have the hash
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
#
#     # password not check with create_user, need the following code
#     @staticmethod
#     def validate_password(data):
#         validators.validate_password(password=data, user=User)
#         return
#
