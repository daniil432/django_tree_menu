from django.db import models


class TreeModel(models.Model):
    title = models.CharField(max_length=255)
    parent = models.IntegerField()
    position = models.IntegerField(default=1)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('MenuCategory', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Содержимое меню"
        verbose_name_plural = "Содержимое меню"
        ordering = ['parent', "id", ]


class MenuCategory(models.Model):
    title = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория меню"
        verbose_name_plural = "Категории меню"
        ordering = ["id", "is_published"]
