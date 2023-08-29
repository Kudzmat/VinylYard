from django import forms


class TrackSearchForm(forms.Form):
    track_name = forms.CharField(label='Track Name', max_length=100)
