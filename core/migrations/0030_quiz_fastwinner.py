# Generated by Django 4.0.5 on 2022-07-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_useranswer_user_alter_useranswer_winnernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='fastwinner',
            field=models.CharField(default=None, max_length=50),
        ),
    ]