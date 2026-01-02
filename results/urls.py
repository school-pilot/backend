from django.urls import path
from . import views

urlpatterns = [
    path('assessments/', views.assessment_list, name='assessment_list'),
    path('scores/', views.enter_scores, name='enter_scores'),
    path('scores/<int:score_id>/', views.update_score, name='update_score'),
    path('class/', views.class_results, name='class_results'),
    path('approve/', views.approve_results, name='approve_results'),
    path('student/<int:student_id>/', views.student_results, name='student_results'),
]
