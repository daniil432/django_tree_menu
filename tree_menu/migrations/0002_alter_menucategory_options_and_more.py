# Generated by Django 4.1.7 on 2023-03-03 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tree_menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="menucategory",
            options={
                "ordering": ["id"],
                "verbose_name": "Категория меню",
                "verbose_name_plural": "Категории меню",
            },
        ),
        migrations.RemoveField(model_name="menucategory", name="is_published",),
    ]
