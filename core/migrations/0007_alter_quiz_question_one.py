# Generated by Django 4.0 on 2022-06-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_quiz_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question_one',
            field=models.CharField(default=0, max_length=115),
        ),
    ]
