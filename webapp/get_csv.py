import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
import django

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

from python_snippets import models

models.PythonSnippet.objects.to_csv("../data/data1.csv")
