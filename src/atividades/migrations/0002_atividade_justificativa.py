# Generated by Django 2.0.7 on 2018-07-12 15:09

import atividades.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='justificativa',
            field=models.FileField(blank=True, null=True, upload_to=atividades.models.user_directory_path),
        ),
    ]
