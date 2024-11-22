# Generated by Django 5.1.3 on 2024-11-22 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('blog', 'Blog'), ('thought', 'Thought')], default='blog', max_length=10, verbose_name='Tipo de Post'),
        ),
    ]
