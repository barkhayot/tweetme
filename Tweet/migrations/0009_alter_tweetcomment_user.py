# Generated by Django 3.2.5 on 2021-07-25 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tweet', '0008_auto_20210725_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
