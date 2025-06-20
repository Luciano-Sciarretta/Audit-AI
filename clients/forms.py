from django.forms import ModelForm
from .models import ClientProfile

class ClientProfileForm(ModelForm):
    class Meta:
        model = ClientProfile
        fields = '__all__'
        exclude = ['created', 'user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'
                