from django import forms

from author.models import Author


class AuthorForm(forms.Form):
    firstName = forms.CharField(
        label='First name',
        required=False
    )
    lastName  = forms.CharField(
        label='Last name',
        required=True
    )
    gender    = forms.ChoiceField(
        choices=Author.GENDER_CHOICES,
        label='Gender',
        required=True
    )


