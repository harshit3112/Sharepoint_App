# Generated by Django 2.2.5 on 2021-03-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_document_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='user',
            new_name='users',
        ),
    ]
