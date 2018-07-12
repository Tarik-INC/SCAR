# Generated by Django 2.0.7 on 2018-07-12 04:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('email', models.EmailField(default='exemplo@exemplo.com', max_length=120, unique=True)),
                ('instituicao', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo', models.CharField(choices=[('masc', 'masculino'), ('fem', 'feminino'), ('open', 'não declarado')], default='open', max_length=20)),
                ('professor', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=200)),
                ('prazo', models.DateTimeField()),
                ('em_equipe', models.BooleanField(default=True)),
                ('trofeu', models.IntegerField(choices=[(3, 'Bronze'), (5, 'Prata'), (7, 'Ouro')], default=1)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
