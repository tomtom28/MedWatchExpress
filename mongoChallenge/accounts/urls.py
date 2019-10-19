from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.CustomSignUp.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
]
