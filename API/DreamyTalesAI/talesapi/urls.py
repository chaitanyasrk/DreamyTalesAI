from django.urls import path
from .views import StoryAPIView

from . import views

urlpatterns = [
    path('story/', views.index, name="story_api"),
]