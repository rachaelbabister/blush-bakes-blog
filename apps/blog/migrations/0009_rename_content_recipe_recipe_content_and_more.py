# Generated by Django 4.2.11 on 2024-05-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_recipe_method_recipe_blurb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='content',
            new_name='recipe_content',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='blurb',
            field=models.TextField(),
        ),
    ]
