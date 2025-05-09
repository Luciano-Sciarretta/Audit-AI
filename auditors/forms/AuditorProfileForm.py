from django.forms import ModelForm
from ..models import AuditorProfile

class AuditorProfileForm(ModelForm):
    class Meta:
        model =AuditorProfile 
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'