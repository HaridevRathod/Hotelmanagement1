# Generated by Django 3.2.5 on 2021-07-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_customerform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerform',
            name='no_of_the_days_to_stay',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='customerform',
            name='room_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
