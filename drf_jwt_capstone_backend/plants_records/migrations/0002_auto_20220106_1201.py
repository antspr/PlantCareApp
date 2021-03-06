# Generated by Django 3.2.8 on 2022-01-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_record',
            name='didChangeDirt',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='plant_record',
            name='didRotate',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='plant_record',
            name='didWater',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='plant_record',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
