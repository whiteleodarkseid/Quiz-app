# Generated by Django 4.0.5 on 2022-07-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_useranswer_fastwinner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='fastwinner',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
    ]
