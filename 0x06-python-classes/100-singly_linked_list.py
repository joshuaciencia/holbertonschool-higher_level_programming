#!/usr/bin/python3
class Node:
    """
    Node for singly linked list
    Attributes:
        data (int): data of node
        next_node (Node): reference node to next in linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter """
        return self.__data

    @data.setter
    def data(self, data):
        """ data setter """
        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """ next node getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """ next node setter """
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """
    singly linked list class
    Attributes:
        head (Node): head node
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        node = self.__head
        linked_list = ""
        while node is not None:
            linked_list += str(node.data) + "\n"
            node = node.next_node
        linked_list = linked_list[:-1]
        return linked_list

    def sorted_insert(self, value):
        """ inserted node sorted """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        nodes = []
        cur = self.__head
        while cur.next_node is not None:
            cur = cur.next_node
        cur.next_node = new
        cur = self.__head
        while cur is not None:
            nodes.append(cur.data)
            cur = cur.next_node
        nodes.sort()
        cur = self.__head
        i = 0
        while cur is not None:
            cur.data = nodes[i]
            cur = cur.next_node
            i += 1
