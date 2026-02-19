from django import forms
from .models import Resume, Role

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'})
        }

class RoleSelectionForm(forms.Form):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="Select Role", widget=forms.Select(attrs={'class': 'form-select'}))

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
