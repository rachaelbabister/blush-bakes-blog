# Generated by Django 4.2.11 on 2024-05-02 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_member_since_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favourites',
            new_name='favourite_recipes',
        ),
    ]
