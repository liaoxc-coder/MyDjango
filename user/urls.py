from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.userLogin, name='userlogin'),
    path('home/<str:uid>/', views.homePage, name='home')
]
