# Generated by Django 2.0.4 on 2018-05-27 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0007_auto_20180527_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='trofeu2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='trofeu2', to='atividades.Trofeu'),
        ),
    ]