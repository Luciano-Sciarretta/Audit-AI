from django.contrib.auth.forms import UserCreationForm
from django import forms
from authentication.models import CustomUser

class ClientCreationForm(UserCreationForm):
    
    email = forms.EmailField(
    required=True,
    widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'input'})
)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_auditor']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,  field in self.fields.items():
            field.widget.attrs.update({ 'class': 'input'})
            if field_name == 'password1' or field_name == 'password2':
                field.widget.attrs.update({'autocomplete': 'new-password'})
                
                
                
                
                
class AuditorCreationForm(UserCreationForm):
    
    email = forms.EmailField(
    required=True,
    widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'input'})
)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_auditor']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,  field in self.fields.items():
            field.widget.attrs.update({ 'class': 'input'})
            if field_name == 'password1' or field_name == 'password2':
                field.widget.attrs.update({'autocomplete': 'new-password'})
                