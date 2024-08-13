from django.urls import path
from . import views

urlpatterns = [
    path('apertura/', views.apertura_view , name='apertura' ),
    path('cierre/', views.cierre_view, name='cierre'),
]
