class Node:
    """Дерево, листья которого могут менять статус всех своих предков на открытый"""
    def __init__(self, id=None, title=None, parent=None, slug=None):
        self.id = id
        self.title = title
        self.parent = parent
        self.slug = slug
        self.children = []
        self.status = 'close'

    def __add__(self, other):
        self.children.append(other)
        return self

    def change_status(self, selected):
        if self.slug == selected:
            self.status = 'open'
            if self.parent != 0:
                self.parent.change_status(self.parent.slug)
        else:
            if self.children is not None:
                for ch in self.children:
                    ch.change_status(selected)
        return self
