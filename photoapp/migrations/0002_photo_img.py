# Generated by Django 3.2.5 on 2021-07-19 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='img',
            field=models.ImageField(default='0', upload_to='pictures'),
            preserve_default=False,
        ),
    ]
