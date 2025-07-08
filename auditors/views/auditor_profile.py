from django.shortcuts import render
from ..models import AuditorProfile
from authentication.models import CustomUser
from django.shortcuts import get_object_or_404

def auditor_profile(request, pk):
    auditor = get_object_or_404(AuditorProfile, id=pk)
    context = {
        'auditor': auditor
    }
    return render(request, 'auditors/auditor-profile.html', context)