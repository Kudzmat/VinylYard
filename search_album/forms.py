from django import forms
from django.core import validators
from .models import *


# form for artist search
class SearchAlbum(forms.Form):
    name = forms.CharField(
        validators=[validators.MaxLengthValidator(15), validators.MinLengthValidator(5)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter an album', 'style': 'width:300px'}),
    )

    class Meta:
        model = Album
        fields = "__all__"  # getting all the fields in the model
