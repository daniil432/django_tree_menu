# Generated by Django 4.1.7 on 2023-03-02 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                ("is_published", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Категория меню",
                "verbose_name_plural": "Категории меню",
                "ordering": ["id", "is_published"],
            },
        ),
        migrations.CreateModel(
            name="TreeModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("parent", models.IntegerField()),
                ("position", models.IntegerField(default=1)),
                ("slug", models.SlugField(unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="tree_menu.menucategory",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Содержимое меню",
                "verbose_name_plural": "Содержимое меню",
                "ordering": ["parent", "id"],
            },
        ),
    ]
