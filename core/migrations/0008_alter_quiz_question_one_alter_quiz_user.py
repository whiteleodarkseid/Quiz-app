# Generated by Django 4.0 on 2022-06-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_quiz_question_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question_one',
            field=models.CharField(blank=True, default=0, max_length=115, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user',
            field=models.CharField(blank=True, default=0, max_length=15, null=True),
        ),
    ]
