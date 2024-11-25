# Generated by Django 5.1.3 on 2024-11-24 14:42

import django.db.models.deletion
import filer.fields.image
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_project_alter_post_tags'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Imágen')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Imágenes del Proyecto',
                'verbose_name_plural': 'Imágenes del Proyecto',
            },
        ),
    ]