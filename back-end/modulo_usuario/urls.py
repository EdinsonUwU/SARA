from django.urls import path
from modulo_usuario import views

urlpatterns = [
    path('alluser/', views.All_user.as_view()),
    path('user_manage/', views.User_manage.as_view()),
    path('usuario/', views.Usuario.as_view()),
    path('usuario_manage/', views.Usuario_manage.as_view()),
]

