# Generated by Django 5.1.2 on 2024-10-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_quizattempt_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizattempt',
            name='total_questions',
            field=models.IntegerField(default=0),
        ),
    ]
