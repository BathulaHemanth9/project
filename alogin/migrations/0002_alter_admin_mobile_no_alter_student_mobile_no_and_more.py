# Generated by Django 5.1 on 2024-09-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='mobile_no',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile_no',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
