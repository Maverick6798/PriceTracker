from django import forms
from pyrsistent import field
from .models import Link

class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ("url","set_price",)