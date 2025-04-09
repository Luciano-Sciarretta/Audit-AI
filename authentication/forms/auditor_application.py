from django import forms
from ..models.auditor import AuditorApplication 

class AuditorApplicationForm(forms.ModelForm):
    class Meta:
        model = AuditorApplication
        fields = ['name', 'surname','document', 'photo', 'location', 'competency', 'iso_standard','email1', 'email2', 'phone', 'documents']
        labels = {
            'name': 'Name',
            'email1': 'Email',
            'email2': 'Confirm your email',
            'phone': 'Phone',
            'documents':'CV and Credentials',
        }
        
        help_texts = {'documents': 'Please upload your document in PDF format (maximum 5MB)'
}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
