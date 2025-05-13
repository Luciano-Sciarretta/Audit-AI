from django.shortcuts import render
from ..models import AuditorProfile

def auditor_profile(request, pk):
    auditor = AuditorProfile.objects.get(id = pk)
    context = {
        'auditor': auditor
    }
    return render(request, 'auditors/auditor-profile.html', context)