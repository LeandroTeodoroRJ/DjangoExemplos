# Generated by Django 5.0.1 on 2024-05-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_alter_author_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
