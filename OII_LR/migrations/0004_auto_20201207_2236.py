# Generated by Django 3.1.4 on 2020-12-07 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OII_LR', '0003_auto_20201207_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidates',
            old_name='age_bit',
            new_name='age_big',
        ),
    ]
