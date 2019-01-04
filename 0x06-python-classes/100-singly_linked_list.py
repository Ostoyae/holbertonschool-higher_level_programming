#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value.__class__.__name__ is not "Node" and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        elif self.__head.data > value:
            self.__head = Node(value, self.__head)
        elif self.__head.data < value:
            node = self.__head
            while node.next_node:
                if node.next_node.data > value:
                    tmp = node.next_node
                    node.next_node = Node(value, tmp)
                    return
                node = node.next_node
            node.next_node = Node(value)

    def __str__(self):
        str = ""
        while self.__head:
            str = str + "{}".format(self.__head.data)
            if self.__head.next_node is not None:
                str = str + "\n"
            self.__head = self.__head.next_node
        return str
