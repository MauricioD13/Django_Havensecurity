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

from django.contrib import admin
from django.urls import path
from dashboard import views as dashboard_views

from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

from users import views as users_views
from havensecurity import views as local_views


def index(request):
    return redirect('haven')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('dashboard_rfid/', dashboard_views.dashboard_rfid, name='dashboard_rfid'),
    path('haven/', local_views.haven, name='haven'),
    path('', index, name='index'),
    path('users/login', users_views.login_view, name='login'),
    path('users/logut', users_views.logout_view, name='logout'),
    path('users/signup', users_views.signup, name='signup'),
    path('details/', local_views.details, name='details'),
    path('about/', local_views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

