from django import forms
from django.forms import ModelForm

from contact.models import AboutUs


class AboutUsForm(ModelForm):
    class Meta:
        model = AboutUs
        fields = ['company', 'address_company', 'phone', 'description']