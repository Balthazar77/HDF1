from django import forms

from organizations.forms import ProfileForm
from organizations.models import DataUserOrganization
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = DataUserOrganization
        fields = ['name_org', 'name_director', 'inn', 'ur_address', 'post_address']