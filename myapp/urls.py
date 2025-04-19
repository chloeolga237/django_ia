# myapp/views.py
from django.shortcuts import render
from textblob import TextBlob  # Si vous utilisez TextBlob pour l'analyse de sentiment

def home(request):
    return render(request, 'myapp/home.html')  # Assurez-vous d'avoir un template 'home.html'

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        analysis = TextBlob(text)
        sentiment = analysis.sentiment
        return render(request, 'myapp/result.html', {'sentiment': sentiment})
    return render(request, 'myapp/analyze.html')  # Formulaire pour l'analyse