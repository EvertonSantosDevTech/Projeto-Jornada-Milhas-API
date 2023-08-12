# Generated by Django 4.2.3 on 2023-08-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0003_destino'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='foto',
        ),
        migrations.AddField(
            model_name='destino',
            name='foto1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='destino',
            name='foto2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='destino',
            name='meta',
            field=models.CharField(default='', max_length=160),
        ),
        migrations.AddField(
            model_name='destino',
            name='texto_descritivo',
            field=models.TextField(blank=True, null=True),
        ),
    ]