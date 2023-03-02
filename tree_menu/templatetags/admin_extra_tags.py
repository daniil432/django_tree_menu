from django import template
from tree_menu.models import TreeModel

register = template.Library()


@register.inclusion_tag('admin/change_form_extra.html', takes_context=True)
def extra_content(context):
    """Данные для таблицы всех пунктов меню"""
    data = TreeModel.objects.all()
    return {
        "table": data,
    }
