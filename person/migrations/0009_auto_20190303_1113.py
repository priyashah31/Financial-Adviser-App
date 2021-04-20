# Generated by Django 2.0.9 on 2019-03-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0008_category_todolist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('mneed', 'Monthly Needs'), ('dneed', 'Daily Need'), ('want', 'Want')], max_length=255),
        ),
    ]
