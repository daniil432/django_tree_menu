from django.contrib import admin
from tree_menu.models import TreeModel, MenuCategory


class TreeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "parent", "position", "category")
    search_fields = ("title", "parent",)
    prepopulated_fields = {"slug": ("title", "position", "category")}

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['include_template'] = 'admin/change_form_include.html'
        return super(TreeModelAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Отрисовка в админ-панели таблицы со всеми уже имеющимися элементами меню
        для более удобного добавления новых элементов с учетом уже существующих.
        """
        extra_context = extra_context or {}
        extra_context['include_template'] = 'admin/change_form_include.html'
        return super(TreeModelAdmin, self).change_view(
         request, object_id, form_url, extra_context=extra_context,
        )


class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")
    search_fields = ("title", "is_published",)


admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(TreeModel, TreeModelAdmin)

admin.site.site_title = 'Админ-панель древовидного меню'
admin.site.site_header = "Админ-панель древовидного меню"
