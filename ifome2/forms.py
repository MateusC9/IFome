
from django import forms
from .models import Lanche


class LancheForm(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ['nome_vendedor', 'produto_oferecido', 'preçodoproduto', 'curso', 'contato', 'foto']