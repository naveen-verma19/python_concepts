#List comprehension
x=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

rows=len(x)
cols=len(x[0])

#list the first column of the 2d array [1,5,9]
first_colums_array =[x[i][0] for i in range(rows)]
second_column_array=[x[i][1] for i in range(rows)]

#so transpose is nothing but array of all these column arrays
xt=[[x[i][j] for i in range(0,rows)] for j in range(0,cols)]
print(xt)

#Set comprehension
x={x**2 for x in range(-50,50)}
print(len(x))

#Dictionary comprehension

x={k:v for k,v in [(1,2),(2,3),(4,6)]}
print(x)