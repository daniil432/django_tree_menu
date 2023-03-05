from django import template
from tree_menu.models import TreeModel
from tree_menu.utils import Node

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_cat):
    """Тег для отрисовки меню, которой можно вызвать в желаемом месте html.

    Формирует структуру данных дерево из queryset, полученного с БД по названию меню.
    Далее в tree_menu/menu.html формируется структура меню через <detail></detail>.
    """
    def create_tree(queryset):
        """Формирование дерева из queryset'а.
        """
        menu_list = []
        tree = {}

        for i in queryset:
            item = Node(id=i['id'], title=i['title'], parent=i['parent'], slug=i['slug'])
            tree[item.id] = item

        for i in queryset:
            obj = i
            if not obj['parent']:
                root = tree[obj['id']]
                menu_list.append(root)
            else:
                parent_id = obj['parent']
                tree[parent_id] += tree[obj['id']]
                tree[obj['id']].parent = tree[parent_id]
                tree[obj['id']].slug = f"{tree[parent_id].slug}/{tree[obj['id']].slug}"

        return menu_list

    # Получение queryset'а из БД по названию меню.
    menu = list(TreeModel.objects.filter(category__title=menu_cat).values())
    menu = create_tree(menu)
    # Изменение статуса текущей вкладки меню и всех её предков на "open".
    for m in menu:
        m.change_status(context['cat_selected'])
    return {
        "menu_items": menu,
    }
