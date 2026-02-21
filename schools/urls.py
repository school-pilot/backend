from django.urls import path
from .views import (
    add_school,
    view_schools,
    view_all_schools,
    update_school,
    create_session,
    view_sessions,
    update_session,
    create_term,
    view_terms,
    update_term,
    get_current_term
    )

urlpatterns = [
    
    path('add/', add_school, name='add_school'),
    path('view/<int:school_id>/', view_schools, name='view_schools'),
    path('update/<int:school_id>/', update_school, name='update_school'),
    path('view-all/', view_all_schools, name='view_all_schools'),
    
    # session urls
    path('session/create/', create_session, name='create_session'),
    path('session/view/<int:school_id>/', view_sessions, name='view_sessions'),
    path('session/update/<int:session_id>/', update_session, name='update_session'),
    path('term/create/', create_term, name='create_term'),
    path('term/view/<int:school_id>/', view_terms, name='view_terms'),
    path('term/update/<int:term_id>/', update_term, name='update_term'),
    path('term/current/<int:school_id>/', get_current_term, name='get_current_term')
]

