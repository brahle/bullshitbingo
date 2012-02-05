from django import forms

from phrase.models import Phrase

class PhraseForm(forms.ModelForm):
    class Meta:
        model = Phrase


