from django import forms
from .models import WebDocument

class WebDocumentForm(forms.ModelForm):
    url = forms.CharField(max_length=2083)
    title = forms.CharField(max_length=255, required=False)

    class Meta:
        model = WebDocument
        fields = ['url', 'title']