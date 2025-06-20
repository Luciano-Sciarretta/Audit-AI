from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import ClientProfile
from .forms import ClientProfileForm
from django.core.exceptions import ValidationError
from django.contrib import messages


def client_profile(request, pk):
    client = get_object_or_404(ClientProfile, pk=pk)
    context = {
       'client': client
    }
    return render(request, 'clients/client-profile.html', context)


def client_edit_account(request, pk):
   client= ClientProfile.objects.get(id = pk)
   
   if request.method == 'POST':
      form = ClientProfileForm(request.POST, request.FILES, instance = client )
      if form.is_valid():
         try:
            form.save()
            messages.success(request, "Prfile actualizado correctamente")
            return redirect('chat')
         except ValidationError as e:

            messages.error(request, "Error al guardar el formulario")
      else:
         messages.error(request, "Formulario no válido")
      
   else:
      form = ClientProfileForm(instance = client)
      context = {'form': form}
      return render(request, 'clients/client-edit-account.html', context)