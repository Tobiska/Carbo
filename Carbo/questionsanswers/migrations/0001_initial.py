# Generated by Django 3.2.8 on 2021-10-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type_answer', models.CharField(choices=[('RAD', 'radio'), ('CHECK', 'checkbox'), ('IN', 'input'), ('COUNT', 'counter')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionsanswers.question')),
            ],
        ),
    ]
