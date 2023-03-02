from django.shortcuts import render


def index(request, cat_slug=None):
    context = {
        "cat_selected": cat_slug,
    }
    return render(request, "tree_menu/index.html", context)
