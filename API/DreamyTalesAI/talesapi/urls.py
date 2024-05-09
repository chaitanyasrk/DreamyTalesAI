from django.urls import path
from .views import StoryAPIView

from . import views

urlpatterns = [
    path('story/', StoryAPIView.as_view(), name='story_api'),
]