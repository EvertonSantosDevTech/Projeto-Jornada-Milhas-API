# Generated by Django 4.2.3 on 2023-07-19 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depoimento',
            old_name='nomeCompleto',
            new_name='nome_completo',
        ),
    ]
