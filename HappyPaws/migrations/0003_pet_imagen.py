# Generated by Django 4.1.7 on 2023-04-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyPaws', '0002_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
