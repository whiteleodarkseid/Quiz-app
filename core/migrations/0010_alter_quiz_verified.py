# Generated by Django 4.0 on 2022-06-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_quiz_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='verified',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]