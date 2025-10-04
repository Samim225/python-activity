# sot = [1,5,3,4,2]
# print(sorted(sot))




# from collections import deque
# q = deque([1,4,6,8])
# q.append(9)
# print(q)

dec = {"words": ["samim","ball","cat","dog"] }
print(len(dec["words"]))
stack = ["samim", 1, "hi", 89]
stack.pop(2)
print(stack)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def add(self, add):
#         new_node = Node(add)
#         if self.next is None:
#             self.next = new_node
#         else:
#             current = self.next
#             while current.next:
#                 current = current.next
#             current.next = new_node

# class Nod2:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def add(self, add):
#         new_node = Nod2(add)
#         if self.next is None:
#             self.next = new_node
#         else:
#             current = self.next
#             while current.next:
#                 current = current.next
#             current.next = new_node
#     def print_list(self):
#         current = self
#         while current:
#             print(current.data)
#             current = current.next
# node1 = Node(5)
# node1.add(8)
# node1.add(9)
# node1.add(10)
# nodd2 = Nod2(1)
# nodd2.add(2)
# nodd2.add(3)
# nodd2.add(4)
# print(nodd2.print_list())


