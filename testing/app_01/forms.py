from app_01.models import UploadFiles
from django import forms

class UploadFilesForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['file']