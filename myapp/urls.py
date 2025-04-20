# myapp/urls.py
from django.urls import path
from . import views  # Assurez-vous que les vues sont importées correctement

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('analyze/', views.analyze_sentiment, name='analyze_sentiment'),  # Gère l'analyse de sentiment
    # La page de résultat n'est plus nécessaire, on affiche les résultats dans analyze.html
]