# Generated by Django 3.2.9 on 2021-11-13 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
