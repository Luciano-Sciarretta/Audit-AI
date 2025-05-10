from django.urls import path
from .views.auditors import AuditorsProfileView, AuditorsView
from .views.auditor_account import auditor_account


urlpatterns = [
    path('', AuditorsView.as_view(), name = 'auditors'),
    # path('auditors-form/',AuditorsProfileView.as_view(), name='auditors-form' ),
    path('auditor-account/', auditor_account, name = 'auditor-account'),
]
