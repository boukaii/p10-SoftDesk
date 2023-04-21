from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul un auteur ou contributeur du projet peut effectuer des opérations"

    def has_object_permission(self, request, view,  obj):

        """On autorise toute les demandes"""
        if request.method in permissions.SAFE_METHODS:
            return True

        """Les autorisations d'écriture ne sont accordées qu'au propriétaire de l'extrait"""
        return obj.contributor == request.user


class IsIssueAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul l'auteur du problème peut le modifier ou le supprimer"

    def has_object_permission(self, request, view,  obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    message = "Seul l'auteur du commentaire peut actualiser ou supprimer"
    # Les commentaires doivent être visibles par tous les contributeurs au projet
    # et par le responsable du projet, mais seul leur auteur
    # peut les actualiser ou les supprimer.

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
