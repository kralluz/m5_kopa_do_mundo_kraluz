from django.urls import path
from .views import TeamsView

urlpatterns = [
    path('teams/', TeamsView.as_view()),
    path('teams/<int:team_id>/', TeamsView.as_view())
]