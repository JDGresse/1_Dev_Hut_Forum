# Generated by Django 4.2.7 on 2023-11-10 15:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0009_remove_post_language_remove_post_linenos_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="like",
            old_name="post",
            new_name="owner",
        ),
    ]
