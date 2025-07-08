from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms.AuditorProfileForm import AuditorProfileForm
from django.contrib import messages
from ..models import AuditorProfile
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='login')
def auditor_account(request):
    
    try:
        auditor = AuditorProfile.objects.get(user = request.user) 
        print(" AUDITOR::::", auditor)
    except ObjectDoesNotExist as e:
        print("ObjectDoesNotExist:", str(e))  
        auditor = None
        
    if request.method == 'POST':
        try:
            form = AuditorProfileForm(request.POST, request.FILES, instance=auditor)

            if form.is_valid():
                user = request.user
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                form.save_m2m()
                messages.success(request, 'Profile updated successfully')
                return redirect('auditors')
            else:
                messages.error(request, "Errores en el formulario")
                context = {'form': form}
                return render(request, 'auditors/auditor-account.html', context)
        except Exception as e:
            messages.error(request, f"Error en la creación del perfíl: {str(e)}")
            print(f"Error en la creación del perfíl: {str(e)}")
            return render(request, 'auditors/auditor-account.html', {'form': form})
    else:
        if auditor:
            form = AuditorProfileForm(instance=auditor)
        else:
            form = AuditorProfileForm()
        context = {'form': form,
                   'auditor': auditor}
        return render(request, 'auditors/auditor-account.html', context)


