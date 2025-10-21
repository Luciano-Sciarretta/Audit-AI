from django.shortcuts import render



def audits(request, pk):
    return render(request, 'auditors/auditor-audits.html')