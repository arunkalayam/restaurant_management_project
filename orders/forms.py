from django import forms
from .models import ContactForm

class Contact(forms.ModelForm):
    class Meta:
        model=ContactForm
        field=['name','emails']