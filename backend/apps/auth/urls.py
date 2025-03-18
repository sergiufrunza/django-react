from django.urls import path
from .views import *

app_name = 'auth'
urlpatterns = [
    path('api/auth/register/', RegisterAPIView.as_view(), name='register'),
    path('api/auth/login/', LoginAPIView.as_view(), name='login'),
    path('api/auth/logout/', LogoutAPIView.as_view(), name='logout'),
]
