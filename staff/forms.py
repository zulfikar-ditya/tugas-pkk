from django import forms

from .models import Uses


class UsesForm(forms.ModelForm):
    
    class Meta:
        model = Uses
        fields = ('month', 'year', 'meter_start', 'meter_end')