# Generated by Django 5.1 on 2024-09-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alogin', '0004_alter_admin_mobile_no_alter_student_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
