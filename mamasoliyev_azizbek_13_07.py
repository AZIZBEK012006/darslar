from os import system 
system("cls")

#   1 masala ------------------------------

# class MyList(list):
#     def remove(self,son):
#         for i in self:
#             if i == son:
#                 super().remove(son)

# lst = MyList((1,2,3,1,2,2,21,1,2,2,3,2,1))

# lst.remove(1)

# print(lst)

#   2 masala ---------------------------------

# class MyList(list):
#     def append(self,son: int):
#         for i in range(len(self)):
#             if self[i] == son:
#                 raise ValueError("ElementDublikationError")               
#             super().append(son)
#             return

# lst = MyList((1,2,3,4,5))
# n = int(input("son kiriting: "))
# lst.append(n)
# print(lst)

#   3 masala ---------------------------------

# class MyList(list):
#     def save(self,son):
#         i = len(self)
#         while i != 0:
#             i -= 1
#             if self[i] != son:
#                 self.remove(self[i])


# lst = MyList([1,2,1,3,4,1,1,2,1,2])
# # n = input("son kiriting: ")
# lst.save(1)
# print(lst)















