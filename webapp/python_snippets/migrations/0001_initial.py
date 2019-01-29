# Generated by Django 2.1.5 on 2019-01-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_id', models.IntegerField(unique=True)),
                ('post_id', models.IntegerField()),
                ('pred_post_block_version_id', models.IntegerField(blank=True, null=True)),
                ('root_post_block_version_id', models.IntegerField()),
                ('length', models.IntegerField()),
                ('line_count', models.IntegerField()),
                ('tags', models.CharField(max_length=2048)),
                ('content', models.TextField()),
                ('last_process_sent', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
