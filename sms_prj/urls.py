"""
URL configuration for sms_prj project.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# -------------------------
# Custom Error Handlers
# -------------------------
handler404 = 'accounts.views.custom_404_view'
handler500 = 'accounts.views.custom_500_view'


# -------------------------
# Swagger Schema Configuration
# -------------------------
schema_view = get_schema_view(
    openapi.Info(
        title="School Management System API",
        default_version='v1',
        description="API documentation for SMS backend",
        contact=openapi.Contact(email="support@edumanage.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# -------------------------
# URL Patterns
# -------------------------
urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Swagger Documentation
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),

    # API Routes
    path('api/accounts/', include('accounts.urls')),
    path('api/schools/', include('schools.urls')),
    path('api/students/', include('students.urls')),
    path('api/teachers/', include('staffs.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/results/', include('results.urls')),
    path('api/fees/', include('fees.urls')),
    path('api/communications/', include('communications.urls')),
    path('api/timetable/', include('timetable.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/subscriptions/', include('subscriptions.urls')),
    path('api/audit/', include('audit.urls')),

    # Optional Manual Docs (you can remove later)
    path(
        'api-docs/',
        TemplateView.as_view(template_name='api_docs.html'),
        name='api_docs'
    ),
    path(
        'api-docs-fields/',
        TemplateView.as_view(template_name='api_docs_fields.html'),
        name='api_docs_fields'
    ),

    # Home
    path(
        '',
        TemplateView.as_view(template_name='index.html'),
        name='home'
    ),
]