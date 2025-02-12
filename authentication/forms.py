from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(
    required=True,
    widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'input'})
)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Company Name'}
        
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username', 'class': 'input'}),
            'password1': forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input'}),
            'password2': forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'input'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input '})