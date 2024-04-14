# Generated by Django 5.0.2 on 2024-04-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_remove_produto_tamanho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tamanho',
            name='nome',
        ),
        migrations.AddField(
            model_name='tamanho',
            name='Tamanho',
            field=models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande'), ('GG', 'Extra Grande')], default=2, max_length=20),
            preserve_default=False,
        ),
    ]