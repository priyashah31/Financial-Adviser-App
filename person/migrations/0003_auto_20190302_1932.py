# Generated by Django 2.0.9 on 2019-03-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20190302_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(choices=[('mneed', 'Monthly Needs'), ('dneed', 'Daily Need'), ('want', 'Want')], max_length=255),
        ),
    ]