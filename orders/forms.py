from django import forms
from .models import ContactForm

class Contacts(forms.ModelForm):
    class Meta:
        model=ContactForm
        field=['name','emails']