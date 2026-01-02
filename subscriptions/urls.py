from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.subscription_plans, name='subscription_plans'),
    path('current/', views.current_subscription, name='current_subscription'),
    path('upgrade/', views.upgrade_subscription, name='upgrade_subscription'),
]
