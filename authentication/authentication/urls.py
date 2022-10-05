from django.contrib import admin
from django.urls import path
from my_user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),
]
