"""havensecurity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Django

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Views

from dashboard import views as dashboard_views
from users import views as users_views


def index(request):
    return redirect('haven')

urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('dashboard/',include(('dashboard.urls','dashboard'), namespace='dashboard')),

    path('users/',include(('users.urls','users'), namespace='users')),
    
    path(
        route='',
        view=TemplateView.as_view(template_name = 'haven/haven.html'),
        name='haven'),
    
    path(
        route='details/',
        view=TemplateView.as_view(template_name= 'haven/details.html'),
        name='details'),
    
    path(
        route='about/',
        view=TemplateView.as_view(template_name='haven/about.html'),
        name="about"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

