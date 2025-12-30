from django.urls import path
from .views import add_school, view_schools, update_school

urlpatterns = [
    path('add/', add_school, name='add_school'),
    path('view/<int:school_id>/', view_schools, name='view_schools'),
    path('update/<int:school_id>/', update_school, name='update_school'),
]

