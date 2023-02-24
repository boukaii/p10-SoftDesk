from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from shop.views import ContributorViewSet, CommentViewSet, IssueViewSet, UserSignUpView, ProjectViewSet
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, basename='projects')

router1 = routers.SimpleRouter()
router1.register('contributors', ContributorViewSet, basename='contributors')
router1.register('issues', IssueViewSet, basename='issues')

router2 = routers.SimpleRouter()
router2.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('rest_framework.urls')),
    # Page de déconnexion
    path('logout/', LogoutView.as_view(), name='logout'),
    # Page d'inscription
    path('signup/', UserSignUpView.as_view(), name='signup'),
    # page de connexion, Obtention de tokens
    path("login/", TokenObtainPairView.as_view(), name="login"),
    # Rafraichissemet du token d'acces
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/', include(router1.urls)),
    path('api/', include(router2.urls)),
]

