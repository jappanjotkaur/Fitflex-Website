# Generated by Django 5.0.4 on 2024-06-02 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_rename_calories_diettrack_calories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diettrack',
            old_name='date',
            new_name='d_ate',
        ),
    ]
