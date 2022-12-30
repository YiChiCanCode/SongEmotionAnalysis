from django import forms
from .models import AudioStored

class AudioForm(forms.ModelForm):
    class Meta:
        model=AudioStored
        fields=['song']