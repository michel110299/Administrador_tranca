# Generated by Django 3.2.5 on 2021-07-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0009_alter_rodada_partida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rodada',
            name='PontosCanastra',
            field=models.IntegerField(verbose_name='Pontos totais de canastra'),
        ),
    ]