import os
from pathlib import Path

# Définition de BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Autres configurations...

DEBUG = True  # Assurez-vous que le mode DEBUG est activé pour le développement

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Ajoutez cette ligne

# Liste des applications installées
INSTALLED_APPS = [
    'django.contrib.admin',  # Nécessaire pour l'administration
    'django.contrib.auth',  # Nécessaire pour l'authentification
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Nécessaire pour les sessions
    'django.contrib.messages',  # Nécessaire pour les messages
    'django.contrib.staticfiles',  # Nécessaire pour les fichiers statiques
    'myapp',  # Remplacez par le nom de votre application
]

# Configuration des middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Doit être avant AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Nécessaire pour l'authentification
    'django.contrib.messages.middleware.MessageMiddleware',  # Nécessaire pour les messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # Cela doit être True
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Contexte pour l'authentification
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Utilisez SQLite ou un autre moteur
        'NAME': BASE_DIR / "db.sqlite3",  # Nom de votre base de données
        # Pour PostgreSQL, utilisez les lignes suivantes :
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'nom_de_votre_base',
        # 'USER': 'gomba',
        # 'PASSWORD': 'votre_mot_de_passe',
        # 'HOST': 'localhost',
        # 'PORT': '5432',
    }
}

# Configuration des fichiers statiques
STATIC_URL = '/static/'  # Ajoutez cette ligne pour les fichiers statiques

# Autres configurations...