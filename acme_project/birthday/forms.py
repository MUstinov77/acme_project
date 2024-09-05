from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'},
            )
        }

    def clean_first_name(self):
        return self.cleaned_data['first_name'].split()[0]