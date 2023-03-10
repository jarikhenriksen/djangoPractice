from django import forms

class PetForm(forms.Form):
    petName = forms.CharField(label='Your pets name', max_length=50)
    petColour = forms.CharField(label='Your pets colour', max_length=50)
    petAge = forms.IntegerField(label='Your pets age', min_value=0, max_value=100)

