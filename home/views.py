from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        if request.user.is_auditor:
            return redirect('auditor-profile', request.user.auditorprofile.id )
        else:
            return redirect('chat')
        
    return render(request, 'home/home.html')

def about_us(request):
    return render(request, 'home/about_us.html')
    