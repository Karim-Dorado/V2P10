"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from projects.views import ProjectViewSet
from issues.views import IssueViewSet
from users.views import UserViewSet
from comments.views import CommentViewSet
from contributors.views import ContributorViewSet

router = SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
users_router = routers.NestedSimpleRouter(router, r'projects', lookup='user')

projects_router.register(r'issues', IssueViewSet, basename='issues')
projects_router.register(r'users', ContributorViewSet)

issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(projects_router.urls)),
    path('api/', include(issues_router.urls)),
    path('api/', include(users_router.urls)),
    path('admin/', admin.site.urls),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
]
