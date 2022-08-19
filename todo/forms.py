from django import forms
from .models import Writing

class Writingform(forms.ModelForm):
    class Meta:
        model = Writing
        fields = '__all__'
