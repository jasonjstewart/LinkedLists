# from linkedlist_api import Node, LinkedList

# ll = LinkedList()
# ll.add(1)
# ll.add(2)
# ll.add(3)
# ll.set(0,0) #0,2,3
# a=ll.get(1) #output 2
# print(a)
# ll.swap(0,2) #Output: 3,1,0
# ll.insert(2,3) #Output: 3,1,0,3
# ll.insert(0,2) #Output: 2,3,1,0,3
# ll.delete(1) #Output: 2,1,0,3
# ll.delete(0) #Output=1,0,3
# # for a in ll:
# #     print(a)
# ll.debug_print()

from linkedlist_api import LinkedList
import csv

#def main():
with open('data_example.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        items = row[0].split(",",1)
        parameters=items[1].split(",")
        action = items[0]
        if action ==  'CREATE':
            print(action,parameters)
            linkedList=LinkedList()
        elif action == 'DEBUG':
            linkedList.debug_print()
        elif action == 'ADD':
            print(action,parameters)
            linkedList.add(parameters[0])
        elif action == 'SET':
            print(action,parameters)
            linkedList.set(int(parameters[0]),parameters[1])
        elif action == 'GET':
            print(action,parameters)
            linkedList.get(int(parameters[0]))
        elif action == 'DELETE' :
            print(action,parameters)
            linkedList.delete(int(parameters[0]))
        elif action == 'INSERT':
            print(action,parameters)
            linkedList.insert(int(parameters[0]),parameters[1])
        elif action == 'SWAP':
            print(action,parameters)
            linkedList.swap(int(parameters[0]),int(parameters[1]))
        else:
            print("Blow up!")

#main()
            




