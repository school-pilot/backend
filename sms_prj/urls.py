"""
URL configuration for sms_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
handler404 = 'accounts.views.custom_404_view'
handler500 = 'accounts.views.custom_500_view'
from django.contrib import admin
from django.urls import path, include
# import templateasview
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('api-docs/', TemplateView.as_view(template_name='api_docs.html'), name='api_docs'),
    path('',TemplateView.as_view(template_name='index.html'), name='home')
]

# Custom error handlers (used when DEBUG=False)

