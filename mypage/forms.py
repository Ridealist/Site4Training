from django import forms
from .models import Excel_File

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Excel_File
        fields = ['upload']