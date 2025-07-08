from django.shortcuts import render, redirect
from django.contrib.auth  import login, authenticate, logout
from django.contrib import messages

def login_company(request):
    
    if request.user.is_authenticated:
        print("DEBUG:", request.user.username, request.user.is_auditor)
        if request.user.is_auditor:
            return redirect('auditors')
        else:
            return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Welcome back!")
            if user.is_auditor:
                return redirect('auditors')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
  
    return render(request, 'authentication/login.html')


def logout_company(request):
    logout(request)
    messages.success(request, 'Logout successfuly')
    return redirect('home')