from django import forms
from ..models.auditor import AuditorApplication 

class AuditorApplicationForm(forms.ModelForm):
    class Meta:
        model = AuditorApplication
        fields = ['name', 'surname','document','location', 'email', 'phone', 'documents']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'documents':'CV and Credentials',
        }
        
        help_texts = {'documents': 'Please upload your documents in PDF format (maximum 5MB)'
}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
