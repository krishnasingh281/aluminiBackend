from django.urls import path
from .views import RegisterUserView, LoginView, logout_view

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
     path('login/', LoginView.as_view(), name='login'),
     path('logout/', logout_view, name= 'logout'),
]
