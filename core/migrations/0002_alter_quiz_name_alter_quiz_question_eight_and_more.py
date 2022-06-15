# Generated by Django 4.0 on 2022-06-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_eight',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_eight_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_eleven',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_eleven_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_five_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_four',
            field=models.TextField(blank=True, default={}, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_four_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_nine',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_nine_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_one',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_one_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_seven',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_seven_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_six',
            field=models.TextField(blank=True, default=[], null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_six_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_ten',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_ten_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_three',
            field=models.TextField(blank=True, default={}, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_three_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_twelve',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_twelve_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_two',
            field=models.TextField(blank=True, default={}, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_two_c',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
