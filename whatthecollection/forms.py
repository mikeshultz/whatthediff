from django import forms
from .models import Collection, CollectionUser

class CollectionForm(forms.ModelForm):
    name = forms.CharField(max_length=256)

    class Meta:
        model = Collection
        fields = ['name', ]

class CollectionUserForm(forms.Form):
    collection_id = forms.IntegerField()
    email = forms.EmailField()
    perms = forms.CharField(max_length=2, required=False)
    
    