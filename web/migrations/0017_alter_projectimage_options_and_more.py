# Generated by Django 5.1.3 on 2024-12-09 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_projectimage_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectimage',
            options={'ordering': ['order_sortable'], 'verbose_name': 'Imágen del Proyecto', 'verbose_name_plural': 'Imágenes del Proyecto'},
        ),
        migrations.AddField(
            model_name='projectimage',
            name='order_sortable',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]
