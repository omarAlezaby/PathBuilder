# Generated by Django 2.0.1 on 2018-01-29 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0022_auto_20180128_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
