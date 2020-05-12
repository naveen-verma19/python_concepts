from person import Person

import random
"""
Sorting Dictionary
"""
dic={
}

for i in range(0,20):
    dic[20-i]={"val1":i,"val2":-i}

#DEBIG TO SEE each object and understand
sorted_tups=sorted(dic.items(),key=lambda x:x[1]["val2"]) #list of sorted tuples [ (k,v) , (k2,v2) ]
sorted_dic={k:v for k,v in sorted_tups}
print(sorted_tups)


"""
Sorting list of Objects
"""
persons=[]
for i in range(0,20):
    persons.append(Person(f"name{i}",age=100-i))

sorted_persons=sorted(persons,key=lambda person:person.age)
print(sorted_persons)

