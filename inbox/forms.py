from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'