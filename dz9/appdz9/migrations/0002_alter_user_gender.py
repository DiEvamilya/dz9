# Generated by Django 4.2.6 on 2023-12-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdz9', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('man', 'man'), ('wuman', 'wuman')], max_length=255),
        ),
    ]
