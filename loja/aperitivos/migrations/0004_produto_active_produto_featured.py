# Generated by Django 5.0.2 on 2024-03-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0003_alter_produto_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]