from django import forms
from tredo.models import Email


class EmailForm(forms.ModelForm):

    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'required': 'true'}),
                           max_length=40,
                           help_text='Imie i Nazwisko...')
    email = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'required': 'true'}),
                            max_length=40, help_text='Email...')
    message = forms.CharField(required=False, max_length=500, help_text='Wiadomosc...')


    class Meta:
        model = Email
        fields = ('name', 'email', 'message')
