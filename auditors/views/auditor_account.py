from django.shortcuts import render
from ..forms.AuditorProfileForm import AuditorProfileForm



def auditor_account(request):
    form = AuditorProfileForm()
    context = {'form': form}
    return render(request, 'auditors/auditor-profile-form.html', context)


