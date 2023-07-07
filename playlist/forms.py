from django import forms
from django.core import validators
from .models import *


# form for artist search
class VibeCheck(forms.Form):
    artist1 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your 1st', 'style': 'width:300px'}),
    )

    artist2 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your 2nd', 'style': 'width:300px'}),
    )

    artist3 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your 3rd artist', 'style': 'width:300px'}),
    )

    artist4 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your 4th artist', 'style': 'width:300px'}),
    )

    artist5 = forms.CharField(
        validators=[validators.MaxLengthValidator(50), validators.MinLengthValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Enter your 5th artist', 'style': 'width:300px'}),
    )

    class Meta:
        model = VibeCheck
        fields = "__all__"  # getting all the fields in the model


class GenrePickForm(forms.Form):
    genre = forms.ChoiceField(label='Genre', choices=[('', '--What You In The Mood For--'),
                                                      ('Indie', 'Indie'),
                                                      ('Pop', 'Pop'),
                                                      ('Country', 'Country'),
                                                      ('Hip-Hop', 'Hip-Hop'),
                                                      ('Workout', 'Workout'),
                                                      ('R&B', 'R&B'),
                                                      ('Chill', 'Chill'),
                                                      ('Christian & Gospel', 'Christian & Gospel'),
                                                      ('Sleep', 'Sleep')
                                                      ])
