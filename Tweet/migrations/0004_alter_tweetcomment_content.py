# Generated by Django 3.2.5 on 2021-07-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0003_auto_20210725_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetcomment',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
