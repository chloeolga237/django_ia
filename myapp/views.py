# myapp/views.py
from django.shortcuts import render
from textblob import TextBlob  # Assurez-vous que TextBlob est installé

def home(request):
    """Affiche la page d'accueil."""
    return render(request, 'myapp/home.html')  # Page d'accueil

def analyze_sentiment(request):
    """Gère l'analyse de sentiment du texte soumis."""
    if request.method == 'POST':
        text = request.POST.get('text')  # Récupère le texte du formulaire
        if text:  # Vérifie si le texte n'est pas vide
            analysis = TextBlob(text)  # Analyse le texte avec TextBlob
            sentiment = analysis.sentiment  # Récupère le sentiment
            return render(request, 'myapp/analyze.html', {'sentiment': sentiment})  # Affiche le résultat dans analyze.html
        else:
            return render(request, 'myapp/analyze.html', {'error': 'Le texte ne peut pas être vide.'})  # Message d'erreur pour texte vide
    return render(request, 'myapp/analyze.html')  # Affiche le formulaire pour l'analyse