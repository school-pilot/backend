from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/promote/', views.promote_student, name='promote_student'),
    path('<int:student_id>/profile/', views.student_profile, name='student_profile'),
    path('bulk-upload/', views.bulk_upload_students, name='bulk_upload_students'),
]
