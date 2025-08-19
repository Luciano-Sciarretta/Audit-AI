from ..forms.AuditorProfileForm import AuditorProfileForm
from django.views.generic import  ListView
from django.contrib import messages
from ..models import AuditorProfile



class AuditorsView(ListView):
    model = AuditorProfile
    template_name = 'auditors/auditors.html'
    context_object_name = 'auditors'
    paginate_by = 8
    
    def get_queryset(self):
        return AuditorProfile.objects.all()

