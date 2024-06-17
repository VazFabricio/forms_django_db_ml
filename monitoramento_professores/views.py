from django.shortcuts import render, redirect
from .forms import SurveyForm

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            response = form.save()
            return redirect('success')
    else:
        form = SurveyForm()
    return render(request, 'forms.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')