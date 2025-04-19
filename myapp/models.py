# myapp/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)  # Titre de l'article
    content = models.TextField()  # Contenu de l'article
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return self.title  # Représentation en chaîne de caractères de l'article