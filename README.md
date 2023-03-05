# django_tree_structure_menu
Реализация в django дервовидного меню с возможностью его редактирования через админ панель.

Меню можно добавлять на html страницу при помощи тегов:
{% load menu_tags %}
{% draw_menu 'Название меню' %}

Запуск: в консоли python3 manage.py runserver

Элементы меню редактируются через админ-панель, для удобства добавления новых пунктов и редактирования 
в админ панель отрисовывается таблица со всеми уже существующими пунктами меню.
