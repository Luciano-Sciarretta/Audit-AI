from django.shortcuts import render, redirect
from ..forms.register import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth  import login
from django.contrib import messages


def register_company(request):
    if request.method == 'POST':
        try:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
            
                if user is not None:
                  login(request, user)
                
                  messages.success(request, f"Registration successful! You are now logged. Welcome {user.username}!")
                  return redirect(reverse_lazy('chat'))
            else:
                print("Errors:", form.errors.as_data())
                

        except Exception as e:
            print(f"Error:  {str(e)}")
            messages.error(request, "An error has ocurred during the registration. Please try again" )
            
    else:    
        form = CustomUserCreationForm()
        
    return render(request, 'authentication/register.html', {'form': form})