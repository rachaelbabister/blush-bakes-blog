# Generated by Django 4.2.11 on 2024-04-23 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_difficulty_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='updated_on',
        ),
    ]
