"""
URL configuration for campushive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Key for login, logout, etc.
    # path('accounts/', include('users.urls')), # 用于注册
    # path('', TemplateView.as_view(template_name="home.html"), name='home'),
    # path('courses/', include('courses.urls', namespace='courses')),
]

urlpatterns += [
    path('accounts/', include('users.urls')), # For signup
]

urlpatterns += [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
]

urlpatterns += [
    path('courses/', include('courses.urls', namespace='courses')),
]