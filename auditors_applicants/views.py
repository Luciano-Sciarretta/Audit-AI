from django.shortcuts import  render, redirect
from .forms import AuditorApplicationForm
from django.contrib import messages


def auditor_application(request):
    if request.method == 'POST':
        form = AuditorApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('application-submitted')
        else:
            messages.error(request, 'Please, check your information')  
    else:
        
        form = AuditorApplicationForm()
    context = {
        'form': form
    }    
    
    return render(request, 'auditors_applicants/auditor-application.html', context)


# Template con mensage de aplicación enviada  con éxito
def application_submitted(request):
    return render(request, 'auditors_applicants/application-submitted.html')