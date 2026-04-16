#================================

import numpy as np

arr1 = np.arange(1 , 10).reshape(3 , 3)
arr2 = np.arange(11 , 31).reshape(4 ,5)
print(arr1)
print(arr2)
#=======Horizontal split
print(np.hsplit(arr1 , 3)) # ye array1 ko coloum wise krdega 3 hisso me divide krddga

#====================Vertical split

print(np.vsplit(arr2 , 2)) # ye vertical split krdega 

#====================memory comparision ===========

import sys

print(sys.getsizeof(arr2)) #128 bytes

#=============Advance Indexing============

arr3 = np.arange(0 , 24).reshape(6 , 4)
print(arr3)
print(arr3[1 : 4])
# print(arr3[0 : 4 : 2]) #impoosibe jo chiaye wo nh arha yhn fancy indexing kam ayegi
print(arr3[[0 , 2 , 3]]) #agar koin pattern follow nh horha data nikalne me whn per fancy indexing used hogi ye row wise data nikala hai
print(arr3[0:6,[0,2,3]]) #rown and coloum batye rows to pori li lakin coloum me fancy indexing ki hai fancy indexing double square bracket k sath hoti hai

print(arr3[1::2]) #practice
print(arr3[[1 , 3 ,5]]) #practice


#=================Boolean Indexing===========>>

arr4 = np.random.randint(-50 , 250 , 30).reshape(5 , 6)
print(arr4)
print(arr4 > 50) #true false me laake dega

#=====================Masking=============>>
print(arr4[arr4 > 50]) # ye true false nh layega abb andar se data nikal k layega jo jo 50 se oper hnge


#===============Find even Numbers==========>>


print(arr4[arr4 % 2 == 0]) #ye even number nikal k dega data nikal k layega

print(arr4[(arr4 % 2 == 0) & (arr4 > 50)]) #multuple condition


#============================Broadcasting===================>>!!




