"""
slicing
li[start(def:0) : end(excluded, def: last) : jump(def 1)]

"""

li=list(range(1,11))
print("li",li)
li[:]=li
print(f"li[:5]{li[:5]}")  #first five
li[1:6] # from index 1 to 5
li[-5:]  #last 5 elements
li[::2] #1,3,5,7,9  #from starting to end take jumps of 2
li[1::2] # 2,4,6,8  # from index1 to end take jumps of 2


first,second,*others=li
print(others)


"""
deleting
"""

li.pop() #removes last number
li.pop(3) #removes at index 3
li.pop(0) #removes first element
li.remove("b") #removes b throws error if not found
del li[2:5]

