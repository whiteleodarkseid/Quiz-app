# Generated by Django 4.0 on 2022-06-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_quiz_name_alter_quiz_question_eight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question_four',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_six',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_three',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_two',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]