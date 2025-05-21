from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms.AuditorProfileForm import AuditorProfileForm
from django.contrib import messages


@login_required(login_url='login')
def auditor_account(request):
    form = AuditorProfileForm()
    if request.method == 'POST':
        try:
            print("Request.POST:", request.POST)
            form = AuditorProfileForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                profile = form.save(commit=False)
                print("Profile:", profile)
                profile.user = user
                profile.save()
                
                context = {'form': profile}
                return redirect('auditors')
            else:
                messages.error(request, "Errores en el formulario")
                context = {'form': form}
                return render(request, 'auditors/auditor-account.html', context)
        except Exception as e:
            messages.error(request, f"Error en la creación del perfíl: {str(e)}")
            return render(request, 'auditors/auditor-account.html', {'form': form})
    else:
        form = AuditorProfileForm()
        context = {'form': form}
        return render(request, 'auditors/auditor-account.html', context)


