from django.shortcuts import render
from ..models import AuditorProfile


def auditor_account(request):
    
    # auditor = AuditorProfile.objects.get(id = pk)
    context = {}
    return render(request, 'auditor-account.html')


