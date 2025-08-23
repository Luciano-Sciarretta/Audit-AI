from django.shortcuts import render
from ..models import AuditorProfile
from authentication.models import CustomUser
from django.shortcuts import get_object_or_404

def auditor_profile(request, pk):
    auditor = get_object_or_404(AuditorProfile, id=pk)
    reviews_up_count = auditor.review_set.filter(value = 'up').count()
    reviews_down_count = auditor.review_set.filter(value = 'down').count()
    context = {
        'auditor': auditor,
        'reviews_up': reviews_up_count,
        'reviews_down': reviews_down_count,
    }
    return render(request, 'auditors/auditor-profile.html', context)