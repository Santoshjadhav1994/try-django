# Generated by Django 3.2.25 on 2024-05-17 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
