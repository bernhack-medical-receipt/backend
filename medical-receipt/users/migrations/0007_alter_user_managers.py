# Generated by Django 4.1 on 2022-08-27 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_user_username_alter_user_email"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
    ]