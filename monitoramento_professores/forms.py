from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        exclude = ['question_5']  # Exclui a pergunta question_5
        widgets = {
            'question_1': forms.RadioSelect(attrs={'empty_label': None}),
            'question_2': forms.RadioSelect(attrs={'empty_label': None}),
            'question_3': forms.RadioSelect(attrs={'empty_label': None}),
            'question_4': forms.RadioSelect(attrs={'empty_label': None}),
            'question_6': forms.RadioSelect(attrs={'empty_label': None}),
            'question_7': forms.RadioSelect(attrs={'empty_label': None}),
            'question_8': forms.RadioSelect(attrs={'empty_label': None}),
            'question_9': forms.RadioSelect(attrs={'empty_label': None}),
            'question_10': forms.RadioSelect(attrs={'empty_label': None}),
            'question_11': forms.RadioSelect(attrs={'empty_label': None}),
            'question_12': forms.RadioSelect(attrs={'empty_label': None}),
            'question_13': forms.RadioSelect(attrs={'empty_label': None}),
        }
