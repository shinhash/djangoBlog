from django.urls import path
from . import views

urlpatterns = [
    path('login_page/', views.login_page, name='login/login_page'),
    path('login_process/', views.login_process, name='login/login_process'),
    path('main_page/', views.main_page, name='login/main_page'),
    path('logout_process/', views.logout_process, name='login/logout_process'),
    path('user_info/', views.user_info, name='login/user_info'),
    path('sign_up/', views.sign_up, name='login/sign_up'),
]
