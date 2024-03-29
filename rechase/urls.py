"""rechase URL Configuration

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
from api.views import GoogleLogin, TeamLeaderboardView, rules
from api.views import getQuestion, verifyAnswer, createTeam, joinTeam, updateDashboardOnLogin, TeamLeaderboardView, Rules, deleteTeam
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('player', views.PlayerView, basename='Players')
# router.register('leaderboard', views.TeamLeaderboardView, basename='Teams')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include(router.urls)),
    # path('accounts/', include('rest_auth.urls')),
    # path('accounts/registration/', include('rest_auth.registration.urls')),
    path('accounts/google/', GoogleLogin.as_view(), name='google_login'),
    path('leaderboard/', TeamLeaderboardView, name='leaderboard'),
    path('dashboard/', updateDashboardOnLogin, name='addEntry'),
    path('hunt/', getQuestion, name="level"),
    path('hunt/submit/', verifyAnswer, name="submit"),
    path('create-team/', createTeam, name="create-team"),
    path('join-team/', joinTeam, name="join-team"),
    path('rules/', rules, name='rules'),
    path('deleteTeam/', deleteTeam, name='delete'),
]
