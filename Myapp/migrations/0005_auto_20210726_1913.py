# Generated by Django 3.2.5 on 2021-07-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_auto_20210726_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerform',
            name='mobile_number',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='customerform',
            name='room_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
