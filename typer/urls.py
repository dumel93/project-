"""typer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from type_page import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^typer/', views.TyperBaseView.as_view(), name="base"),
    url(r'^index', views.TyperIndexView.as_view(), name="index"),
    url(r'^login/', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/',views.UserLogoutView.as_view(), name='logout'),
    url(r'^create/', views.UserCreateView.as_view(), name ='create')





] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
