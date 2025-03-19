
app_name = 'blog'

from django.urls import path
from .views import (BlogListCreateAPIView,
                    BlogGetPutDeleteAPIView,
                    BlogLikeAPIView,)


urlpatterns = [
    path('blogs/', BlogListCreateAPIView.as_view()),
    path('blogs/<int:id>/', BlogGetPutDeleteAPIView.as_view()),
    path('blogs/<int:id>/like/', BlogLikeAPIView.as_view()),
]
