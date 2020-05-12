arr=[1,2,3]
b=arr  #referenced
b.append(1)
print(arr)

c=[*arr]  #copied

#copying sets
a={1,2,3,5}
b={*a,7}
b.add(6) #does not affect a



#copying dictionaries
dic={"x":1,"y":2}
dic2=dic  #referenced
dic2['x']=9
dic3 = {**dic,"z":5} #copy
dic2['x']=12

li=[1,2,4,5]
first,second,*others=li

print(others)
