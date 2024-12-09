# Generated by Django 5.1.3 on 2024-12-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_projectimage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='width',
            field=models.CharField(choices=[('25pct', '25% ancho'), ('50pct', '50% ancho'), ('100pct', '100% ancho')], default='100pct', max_length=10, verbose_name='Ancho'),
        ),
    ]
