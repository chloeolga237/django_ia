# myapp/forms.py
from django import forms # type: ignore

class SentimentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Texte à analyser')
