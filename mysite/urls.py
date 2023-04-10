"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include,re_path
from django1stapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('database/', admin.site.urls),
    path('pour1/', views.pour1),
    path('pour2/', views.pour2),
    path('upload_pour1/', views.upload_file_pour1),
    path('upload_pour2/', views.upload_file_pour2),
    path('', views.login),
    path('admin_page/', views.admin_page),
    path('customer_page/', views.customer_page),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),


]
#if settings.DEBUG:
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
