# Generated by Django 4.0 on 2022-06-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_quiz_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='user',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
