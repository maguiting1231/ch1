import numpy as np

import matplotlib.pyplot as plt
import os
import random
list_data=[]
lis_data=[]
lis1_data=[]
list1=[]
list2=[]
lis1=[]
lis2=[]
l1_data=[]
l2_data=[]
i=0
num=0
number=0
x=0
test_list=['idkp1-10.txt']
file_path=r'C:\Users\Lenovo\Desktop\idkp1-10.txt'
#print(list1)
with open(file_path) as file_object:
    while True:
        lines=file_object.readline()
        if ("******* The end *********")in lines:
            break
        if("IDKP") in lines:
           for b in lines:
               if b.isdigit():
                   number=b
           lines=next(file_object)
           for a in lines:
               if a.isdigit()or a=="*" or a==",":
                   list_data.append(a)
           list_data.append(',')
           #print(list_data)
           i=0
           while i<2: 
              lines=next(file_object)
              i=i+1
           str1=lines.strip('\n')
           lis_data=str1.split(',')
           list1.append(lis_data)
           
           lines=next(file_object)
           lines=next(file_object)
           str1=lines.strip('\n')
           lis1_data=str1.split(',')
           list2.append(lis1_data)
print(list2)

t=''
with open('3.txt','w') as q:
    for j in list1:
        for e in range(len(j)):
            t=t+str(j[e])+' '
        q.write(t.strip(' '))
        q.write('\n')
        t=' '
        print('profit写入成功！')

u=''
with open('4.txt','w') as q:
    for j in list2:
        for e in range(len(j)):
            u=u+str(j[e])+' '
        q.write(u.strip(' '))
        q.write('\n')
        u=' '
        print('weight写入成功！')
with open('3.txt','r') as p:
   # while True:
      first_line=p.readline().strip('\n')
     
    
with open('4.txt','r') as p:
    #while True:
     first1_line=p.readline().strip('\n')
x_value=list(first_line.split(' '))
y_value=list(first1_line.split(' '))
x=x_value
y=y_value
#y=['7.1','7.2','7.3','7.4','7.5']
x_value=list(first_line.split(' '))
y_value=list(first1_line.split(' '))
for i in range(len(x_value)):
    print(x_value[i]+x_value[i+1])
fig=plt.figure()
x=np.random.randn(x_value)
plt.scatter(x_value,y_value)

plt.show()
c=list(zip(first_line.split(' '),first1_line.split(' ')))

z=2
A=[]
B=[]
B1=[]
C=[]
C1=[]
while z<len(c):
    A.append(c[z])
    z=z+3
for i in range(len(A)):
   # for j in range(len(A[i])):
        B.append(int(A[i][0])/int(A[i][1]))
        B1.append(i)
C=list(zip(B1,B))
C.sort(key=lambda x:(x[1]))
#C=sorted(B)
#print(C)
for i in range(len(C)):
    C1.append(A[C[i][0]])
C1.reverse()
print('对价值：重量按非递增排序：')
print(C1)

