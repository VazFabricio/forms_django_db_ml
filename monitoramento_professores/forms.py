from django import forms
from .models import SurveyResponse

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = '__all__'
        widgets = {
            'question_1': forms.RadioSelect,
            'question_2': forms.RadioSelect,
            'question_3': forms.RadioSelect,
            'question_4': forms.RadioSelect,
            'question_5': forms.RadioSelect,
            'question_6': forms.RadioSelect,
            'question_7': forms.RadioSelect,
            'question_8': forms.RadioSelect,
            'question_9': forms.RadioSelect,
            'question_10': forms.RadioSelect,
            'question_11': forms.RadioSelect,
            'question_12': forms.RadioSelect,
            'question_13': forms.RadioSelect,
        }

    def clean(self):
        cleaned_data = super().clean()
        for i in range(1, 14):
            question = 'question_{}'.format(i)
            print(cleaned_data[question])
        return cleaned_data
