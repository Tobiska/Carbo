# Generated by Django 3.2.8 on 2021-11-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionsanswers', '0004_auto_20211031_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='enum',
            field=models.TextField(default='null', max_length=255, verbose_name='Unique str identifier'),
        ),
        migrations.AddField(
            model_name='question',
            name='enum',
            field=models.TextField(default='null', max_length=255, verbose_name='Unique str identifier'),
        ),
    ]
