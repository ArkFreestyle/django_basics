from django import forms

class BasicForm(forms.Form):
    latitude = forms.FloatField(label='latitude')
    longitude = forms.FloatField(label='longitude')