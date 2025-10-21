from django.urls import path
from .views.auditors import AuditorsView
from .views.auditor_account import auditor_account
from .views.auditor_profile import auditor_profile
from .views.audits_views import audits


urlpatterns = [
    path('', AuditorsView.as_view(), name = 'auditors'),
    path('auditor-profile/<str:pk>/', auditor_profile, name = 'auditor-profile' ),
    path('auditor-edit-account/', auditor_account, name = 'auditor-edit-account'),
    path("auditor-profile/<str:pk>/audits/", audits, name="auditor_audits"),
]
