# Generated by Django 2.1.5 on 2019-01-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_snippets', '0003_auto_20190129_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythonsnippet',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
