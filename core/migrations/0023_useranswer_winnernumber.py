# Generated by Django 4.0.5 on 2022-07-06 22:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_useranswer_winneraccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='winnernumber',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None),
        ),
    ]
