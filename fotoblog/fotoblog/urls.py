"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

import authentification.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # APP - Authentification ----------------------------------------
    path('', LoginView.as_view(
        template_name='authentification/login.html',
        redirect_authenticated_user=True),
        name='login'),

    path('logout/', authentification.views.logout_user,name='logout'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('user/<int:id>/password-change/', authentification.views.change_user_password, name='password-change'),

    # APP - Blog ----------------------------------------------------
    path('home/', blog.views.home, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)