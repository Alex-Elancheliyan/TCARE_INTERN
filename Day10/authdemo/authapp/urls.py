from django.urls import path
from authapp import views

urlpatterns = [

    path('homepage/',views.homepage, name=""),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout',views.log_out, name='logout'),
  
]
