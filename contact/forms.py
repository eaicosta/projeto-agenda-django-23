from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    # 1° Método
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda'
    )

    # 2° Método
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',

        # })

    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone',
        # 3° Método
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()
