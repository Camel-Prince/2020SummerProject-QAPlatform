from django.urls import path, re_path
from . import views

urlpatterns = [
    path('init/', views.InitView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('detail/', views.UserDetail.as_view()),
    path('home/', views.HomeView.as_view()),
    path('office/', views.OfficeHomeView.as_view()),
    path('msg/', views.MsgView.as_view()),
    re_path(r'^office/room/(?P<pk>.*)/upload', views.OfficeUpLoadImg.as_view()),
    re_path(r'^office/room/(?P<pk>.*)/$', views.OfficeRoomView.as_view()),
]
