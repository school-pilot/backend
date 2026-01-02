from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.create_category, name='create_category'),
    path('structures/', views.assign_fees, name='assign_fees'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('payments/', views.record_payment, name='record_payment'),
    path('payments/history/', views.payment_history, name='payment_history'),
]
