# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze/', include('myapp.urls')),  # Inclure les URLs de myapp
    path('', include('myapp.urls')),  # Rediriger la racine vers myapp
]