"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'student'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete,name='delete'),
    path('signup', views.signup, name='signup'),
    path('fees',views.fees, name='fees'),
    path('feededit/<int:pk>/',views.feededit, name='feededit'),
    path('showfees',views.showfees, name='showfees'),
    path('feesdelete/<int:pk>/',views.feesdelete, name='feesdelete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
