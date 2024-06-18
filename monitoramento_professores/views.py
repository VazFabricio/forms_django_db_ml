from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse
import joblib

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Excluir a pergunta question_5 do dicionário de dados antes de salvar
            cleaned_data = form.cleaned_data
            cleaned_data.pop('question_5', None)
            
            response = SurveyResponse.objects.create(**cleaned_data)
            
            try:
                model = joblib.load('monitoramento_professores/best_model.sav')
            except FileNotFoundError:
                return render(request, 'error.html', {'error_message': 'Modelo não encontrado'})
            
            # Prever a classe da resposta
            input_data = [cleaned_data['question_1'], cleaned_data['question_2'], cleaned_data['question_3'],
                          cleaned_data['question_4'], cleaned_data['question_6'], cleaned_data['question_7'],
                          cleaned_data['question_8'], cleaned_data['question_9'], cleaned_data['question_10'],
                          cleaned_data['question_11'], cleaned_data['question_12'], cleaned_data['question_13']]
            
            try:
                predicted_class = model.predict([input_data])[0]
            except AttributeError:
                return render(request, 'error.html', {'error_message': 'Erro ao fazer a previsão'})
            
            # Salvar a classe prevista no banco de dados
            response.predicted_class = predicted_class
            response.save()
            
            return redirect('success')
    else:
        form = SurveyForm()
    return render(request, 'forms.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')


def control_panel_view(request):
    responses = SurveyResponse.objects.all()
    for response in responses:
        print(response.professor_name, response.predicted_class)
    return render(request, 'control_panel.html', {'responses': responses})