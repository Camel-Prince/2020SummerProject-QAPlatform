from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('detail/', views.UserDetail.as_view()),
    path('home/', views.HomeView.as_view()),
    path('office/', views.OfficeHomeView.as_view()),
]
