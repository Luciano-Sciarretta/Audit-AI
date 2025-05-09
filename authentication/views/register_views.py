from django.shortcuts import render, redirect
from authentication.forms import ClientCreationForm, AuditorCreationForm
from django.urls import reverse_lazy
from django.contrib.auth  import login
from django.contrib import messages


def register_client(request):
    if request.method == 'POST':
        try:
            form = ClientCreationForm(request.POST)
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
                return redirect('register-client')
                

        except Exception as e:
            print(f"Error:  {str(e)}")
            messages.error(request, "An error has ocurred during the registration. Please try again" )
            return redirect('register-client')
            
    else:    
        form = ClientCreationForm()
        context = {'registration_type': 'client', 'form': form}
    return render(request, 'authentication/client-register.html', context)


def register_auditor(request, uuid):
    if request.method == 'POST':
        try:
            form = AuditorCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                
                if user is not None:
                    login(request, user)
                    return redirect('auditors')
                else:
                    messages.error(request, "Registration failed unexpectedly")
                    return render(request, 'authentication/register.html', 
                            {'form': form, 'registration_type': 'auditor'})
            else:
                messages.error(request, "Please correct the errors below")
                return render(request, 'authentication/register.html',
                           {'form': form, 'registration_type': 'auditor'})       
        except Exception as e:
            print("Error:", str(e))
            messages.error(request, "An error has ocurred during the registration. Please try again" )
            return redirect('register-auditor')
            
    else:
        form = AuditorCreationForm()
        context = {'registration_type': 'auditor', 'form': form}
        return render(request, 'authentication/auditor-register.html', context)