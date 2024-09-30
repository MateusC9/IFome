from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')
    repetir_senha = forms.CharField(widget=forms.PasswordInput, label='Repetir Senha')

    class Meta:
        model = User
        fields = ['username', 'senha', 'repetir_senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        repetir_senha = cleaned_data.get('repetir_senha')

        if senha != repetir_senha:
            raise forms.ValidationError("As senhas não coincidem.")
