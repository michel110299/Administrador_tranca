# Generated by Django 3.2.5 on 2021-07-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('DataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'db_table': 'pessoa',
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('DataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('Pessoas', models.ManyToManyField(to='adm.Pessoa')),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
        ),
    ]
