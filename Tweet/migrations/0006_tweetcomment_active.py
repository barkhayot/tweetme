# Generated by Django 3.2.5 on 2021-07-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0005_alter_tweetcomment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetcomment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
