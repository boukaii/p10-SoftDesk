
from rest_framework import permissions

# Un projet ne doit être accessible qu'à son responsable et aux contributeurs.


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul un auteur ou contributeur du projet peut effectuer des opérations"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user