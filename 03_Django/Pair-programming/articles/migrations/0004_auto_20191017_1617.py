# Generated by Django 2.2.6 on 2019-10-17 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20191017_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='article',
        ),
    ]