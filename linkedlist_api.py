#!/usr/bin/env python3
#webites used to understand code
#https://www.geeksforgeeks.org/linked-list-set-1-introduction/
#https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python
#https://www.pythoncentral.io/singly-linked-list-insert-node/


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire list.'''
        print('{} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ])))


    def __iter__(self):
        '''Iterates through the linked list, implemented as a generator.'''
        for node in self._iter_nodes():
            yield node.value


    def _iter_nodes(self):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current
            current = current.next


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''


    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        #create new node and self.head= new node and size+=1
        if (self.head == None):
            self.head = Node(item) 
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(item)
        self.size+=1
        return self.head
        #when node.next=None then add it use a while loop

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if index<self.size:
            current = self.head
            count = 0
            while count < index-1:
                current = current.next
                count+=1
            node = Node(item)
            if index == 0:
                node.next=self.head
                self.head = node
            else:   
                node.next=current.next
                current.next = node
            self.size+=1
        else:
            print("Index out of range")



    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index<self.size:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count+=1
            current.value = item
        else:
            print("Index is out of range")
 


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index<self.size:
            current = self.head
            count = 0
            while count < index:
                current = current.next
                count+=1
            return current.value
        else:
            print("Index out of range")

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if index<self.size:
            current1 = self.head
            count = 0
        
            while count < index:
                current1 = current1.next
                count+=1
            current2 = self.head
            count=0
            while count < index-1:
                current2 = current2.next
                count+=1
            if index == 0:
                self.head = current1.next
            else:
                current2.next=current1.next
            self.size-=1
        else:
            print("Index out of range.")

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if index1 <= self.size and index2 < self.size:
            current1 = self.head
            count= 0
            item1 = 0
            item2 = 0
        
            while count < index1:
                current1 = current1.next
                count+=1
            if index1 !=0:
                item1 = current1.value
            else:
                item1=self.head.value
            current2 = self.head
            count=0
            while count < index2:
                current2 = current2.next
                count+=1
            item2 = current2.value
            current1.value=item2
            current2.value = item1
        else:
            ("Index out of range.")



######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
