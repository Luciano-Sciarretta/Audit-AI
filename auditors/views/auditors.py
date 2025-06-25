from django.shortcuts import render, redirect
from ..forms.AuditorProfileForm import AuditorProfileForm
from django.views.generic import FormView, ListView
from django.contrib import messages
from ..models import AuditorProfile
from django.contrib.auth.mixins import LoginRequiredMixin


class AuditorsView(ListView):
    model = AuditorProfile
    template_name = 'auditors/auditors.html'
    context_object_name = 'auditors'
    paginate_by = 6
    
    def get_queryset(self):
        return AuditorProfile.objects.all()



# class AuditorsProfileView(LoginRequiredMixin, FormView):
#     template_name = 'auditors/auditor-profile-form.html'
#     form_class = AuditorProfileForm
    
#     def form_valid(self, form):
#         try:
#             if AuditorProfile.objects.filter(user=self.request.user).exists():
#                 messages.error(self.request, 'An auditor profile already exists for this user.')
#                 return self.form_invalid(form)
            
#             auditor_profile = form.save(commit= False)
#             auditor_profile.name = auditor_profile.name.lower()
#             auditor_profile.user = self.request.user
#             auditor_profile.save()
#             messages.success(self.request, 'Your profile has been created successfully!')
#             return redirect('auditors')
        
#         except Exception as e:
#             messages.error(self.request, f'Error creating profile: {str(e)}')
#             return self.form_invalid(form)