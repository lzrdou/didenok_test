# Generated by Django 3.1.14 on 2023-10-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordforservice',
            name='encrypted_password',
            field=models.TextField(blank=True, db_column='encrypted_password'),
        ),
    ]