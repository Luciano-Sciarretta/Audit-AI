from django.urls import path
from .views.auditors import AuditorsView
from .views.auditor_account import auditor_account
from .views.auditor_profile import auditor_profile


urlpatterns = [
    path('', AuditorsView.as_view(), name = 'auditors'),
    path('auditor-profile/<str:pk>', auditor_profile, name = 'auditor-profile' ),
    path('auditor-edit-account/', auditor_account, name = 'auditor-edit-account'),
]
