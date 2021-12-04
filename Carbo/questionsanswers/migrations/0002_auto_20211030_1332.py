# Generated by Django 3.2.8 on 2021-10-30 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionsanswers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='next_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='questionsanswers.question'),
        ),
        migrations.AddField(
            model_name='question',
            name='next_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questionsanswers.question'),
        ),
    ]