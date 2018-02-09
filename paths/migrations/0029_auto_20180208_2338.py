# Generated by Django 2.0.2 on 2018-02-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0028_auto_20180206_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-access_counter']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-access_counter'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
        migrations.AlterModelOptions(
            name='path',
            options={'ordering': ['-access_counter']},
        ),
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]
