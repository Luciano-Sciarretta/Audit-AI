from django.shortcuts import render, redirect
from .forms import MessageForm
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from .models import Message
from authentication.models import CustomUser
from .forms import MessageForm
from django.urls import reverse_lazy


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'inbox/message-form.html'
    
    
    def dispatch(self, request, *args, **kwargs):
        self.recipient = get_object_or_404(CustomUser, pk = kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        sender = self.request.user
        form.instance.sender = self.request.user
        form.instance.recipient = self.recipient 
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Errores en el formulario:", form.errors)
        print("Errores generales:", form.non_field_errors())
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipient'] = self.recipient
        return context
    
    
    
    def get_success_url(self):
        try:
            return reverse_lazy('inbox')
        except:
            return reverse_lazy('home')
    
def inbox(request):
    total_messages = Message.objects.filter(recipient = request.user)
    
    context = {
               'total_messages': total_messages
               }
    return render(request, 'inbox/inbox.html', context)


def single_message(request, pk):
    single_message = Message.objects.get(id = pk)
    single_message.is_read = True
    single_message.save()
    context = {'single_message': single_message}
    return render(request, 'inbox/single-message.html', context)



# def get_success_url(self):
#         if hasattr(self.recipient, 'auditorprofile'):
#             return reverse_lazy('auditor-profile', kwargs={'pk': self.recipient.auditorprofile.id})
        
#         elif hasattr(self.recipient, 'clientprofile'):
#             return reverse_lazy('client-profile', kwargs={'pk': self.recipient.clientprofile.id})
#         else:
#             # Por si acaso el usuario no tiene perfil (backup)
#             return reverse_lazy('home')