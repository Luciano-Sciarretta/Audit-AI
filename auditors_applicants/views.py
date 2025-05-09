from django.shortcuts import  render, redirect
from .forms import AuditorApplicationForm


def auditor_application(request):
    if request.method == 'POST':
        form = AuditorApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('application-submitted')
        else:
            print("Formulario no válido")    
    else:
        
        form = AuditorApplicationForm()
    context = {
        'form': form
    }    
    
    return render(request, 'authentication/auditor-application.html', context)


# Template con mensage de aplicación enviada  con éxito
def application_submitted(request):
    return render(request, 'authentication/application-submitted.html')