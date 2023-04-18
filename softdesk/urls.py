from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from projects.views import ContributorViewSet, CommentViewSet, IssueViewSet, UserSignUpView, ProjectViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LogoutView

router = routers.SimpleRouter(trailing_slash=True)
router.register(r"project/?", ProjectViewSet, basename="project")

users_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
users_router.register(r"users/?", ContributorViewSet, basename="users")

issue_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
issue_router.register(r"issue/?", IssueViewSet, basename="issue")

comment_router = routers.NestedSimpleRouter(issue_router, r"issue/?", lookup="issue")
comment_router.register(r"comment/?", CommentViewSet, basename="comment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'', include(router.urls)),
    path(r'', include(users_router.urls)),
    path(r'', include(issue_router.urls)),
    path(r'', include(comment_router.urls)),
]
