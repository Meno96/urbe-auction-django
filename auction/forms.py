from django.forms import ModelForm
from .models import AddUriToArrayForm
from django import forms

# Custom form to add name and image URI to an array
class AddUriToArray(forms.Form):
        # Define form fields
        name = forms.CharField(max_length=30)
        image = forms.ImageField()
        
        # Validate form data
        def clean(self):
            cleaned_data = super().clean()
            name = self.cleaned_data.get('name')
            image = cleaned_data.get('image')
            return cleaned_data
        