# Generated by Django 4.0.5 on 2022-07-06 22:19

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_useranswer_winnernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='winnernumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
