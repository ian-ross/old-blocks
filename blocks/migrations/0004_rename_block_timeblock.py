# Generated by Django 3.2.5 on 2022-01-15 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0003_block_note'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Block',
            new_name='TimeBlock',
        ),
    ]