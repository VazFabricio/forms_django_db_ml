from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_view, name='survey'),
    path('success/', views.success_view, name='success'),
    path('control_panel/', views.control_panel_view, name='control_panel')
]
