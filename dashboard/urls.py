
# Django
from django.urls import path

# Views
from dashboard import views

urlpatterns = [
    
    path(
        route='dashboard',
        view=views.dashboard, 
        name='dashboard'),
    path(
        route='rfid',
        view=views.dashboard_rfid,
        name='dashboard_rfid'),
    
]