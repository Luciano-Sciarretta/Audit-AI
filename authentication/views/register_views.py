from django.shortcuts import render, redirect
from ..forms.register import CompanyCreationForm,AuditorCreationForm
from django.urls import reverse_lazy
from django.contrib.auth  import login
from django.contrib import messages


def register_company(request):
    if request.method == 'POST':
        try:
            form = CompanyCreationForm(request.POST)
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
                return redirect('register')
                

        except Exception as e:
            print(f"Error:  {str(e)}")
            messages.error(request, "An error has ocurred during the registration. Please try again" )
            return redirect('register')
            
    else:    
        form = CompanyCreationForm()
        context = {'registration_type': 'company', 'form': form}
    return render(request, 'authentication/register.html', context)


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
                    return redirect('chat')
                else:
                    messages.error(request, "Registration failed unexpectedly")
                    return render(request, 'authentication/register.html', 
                            {'form': form, 'registration_type': 'auditor'})
                    
        except Exception as e:
            print("Error:", str(e))
            messages.error(request, "An error has ocurred during the registration. Please try again" )
            return redirect('register')
            
    else:
        form = AuditorCreationForm()
        context = {'registration_type': 'auditor', 'form': form}

        return render(request, 'authentication/register.html', context)