class EmptyTreeError(Exception):
    """Узел не найден"""
    pass


class NodeNotFoundError(Exception):
    """Дерево пустое"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, value) -> None:
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_node_recursive(self.root, value)

    def _add_node_recursive(self, current_node, value) -> None:
        """
        Рекурсивно ищет правильное место для нового узла и вставляет его.
        :param current_node: текущий узел начиная с которого выполняется поиск
        :param value: Значение нового узла который нужно вставить
        """
        if value < current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._add_node_recursive(current_node.left, value)
        elif value > current_node.val:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._add_node_recursive(current_node.right, value)
        else:
            print("Добавление не требуется")
            return

    def delete_node(self, value) -> None:
        if self.root is None:
            raise EmptyTreeError("Невозможно удалить узел из пустого дерева.")

        self._delete_node_recursive(self.root, value)

    def _delete_node_recursive(self, current_node, value) -> TreeNode | None:
        """
        Рекурсивно ищет узел для его удаления.
        :param current_node: текущий узел начиная с которого выполняется поиск
        :param value: Значение узла который нужно удалить
        """
        if current_node is None:
            raise NodeNotFoundError(f"Узел со значением {value} не найден в дереве")

        if value < current_node.val:
            current_node.left = self._delete_node_recursive(current_node.left, value)
        elif value > current_node.val:
            current_node.right = self._delete_node_recursive(current_node.right, value)
        else:
            # узел без потомков
            if current_node.left is None and current_node.right is None:
                return None

            # 1 потомок
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # 2 потомка
            else:
                min_node = self._min_node(current_node.right)
                current_node.val = min_node.val
                current_node.right = self._delete_node_recursive(current_node.right, min_node.val)

        return current_node

    def _min_node(self, current_node):
        """Поиск узла с минимальным значением"""
        while current_node.left:
            current_node = current_node.left
        return current_node

    def print_tree(self):
        if self.root is None:
            print("Дерево пустое.")
        else:
            self._print_tree_recursive(self.root, level=0)

    def _print_tree_recursive(self, node, level):
        """
        Выводит узлы дерева, добавляя отступы для отображения уровня.
        :param node: Текущий узел для вывода.
        :param level: Текущий уровень узла, используется для отступов.
        """
        if node is not None:
            self._print_tree_recursive(node.right, level + 1)
            print("    " * level + f"-> {node.val}")
            self._print_tree_recursive(node.left, level + 1)

    def _get_max_deep(self, node):
        if node is None:
            return 0
        else:
            left = self._get_max_deep(node.left)
            right = self._get_max_deep(node.right)

            return max(left, right) + 1
