# Generated by Django 5.1.3 on 2024-11-24 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_projectimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Posts', 'verbose_name_plural': 'Post'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterModelOptions(
            name='projectimage',
            options={'verbose_name': 'Imágen del Proyecto', 'verbose_name_plural': 'Imágenes del Proyecto'},
        ),
    ]
