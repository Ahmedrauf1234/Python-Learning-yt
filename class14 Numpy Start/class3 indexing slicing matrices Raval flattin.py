import numpy as np


arr1 = np.arange(3 , 19)
arr2 = np.random.randint(91 , 198 , 36).reshape(6 , 6)
print(arr1)
print(arr2)
print(np.var(arr1)) #mean nikalega pehle suppose 121 mean aya har num minus hoga 121 se or sabraction k bad jo ans ayega us ka square krliyega ||varience batata hai hamare data me varition kitni hai kitna spread hai data
print(np.std(arr1)) #standard deviation means itno jagah per data spread hva va hai

#======================Trignometric functions===================>>
arr3 = np.arange(1 , 10)
print(np.sin(arr1)) # 1 se lkr 9 tk ki sin ki value dedega
print(np.cos(arr1))
print(np.tan(arr1))

#==================DOt Product===============>>

arr4 = np.arange(1 , 26).reshape(5 , 5)
arr5 = np.arange(26 , 51).reshape(5 , 5)

print(np.dot(arr4 , arr5))
print(np.log(arr1)) #ye log nikal dega
print(np.exp(arr1)) # is ka answer 3**x ki sorat bme mil rha e ki constant value hai 2.71828 or x hamari array ka number hai 

#=======================Indexing and slicing======================>>

arr6 = np.arange(1 , 26).reshape(5 , 5)
print(arr6)
print(arr6[3 , 3]) #3rd row 3rd coloum se mene 19 ko get kra
print(arr6[3 , -2]) #same answer

#===========#3D indexing(jhn depth ajaye wo 3 dimention hojati array)===============

a1 = np.arange(1 , 9).reshape(2 , 2 , 2) #(depth,layers,times) , row , coloum
print(a1)
print(a1[1 , 1 ,1 ]) # depth rows coloum get 8

a2 = np.arange(1 , 13).reshape(3 , 2 , 2)
print(a2[2 , 0 , 0]) # 2 depth 0 row 0 coloum 9 get


#=====================2D Slicing=============>>
#array name[rows , coloum]
#array name[starting: ending:step , starting: ending:step]


a3 = np.random.randint(91 , 198 , 36).reshape(6 , 6)
print(a3)
print(a3[0 : 2 ,0 : 2 ]) #0:2 ye rows ko bata raha or 2nd wala 0:2 ye coloum ko bata rha
# print(a3[:2 , :2]) #most frequent version smart work hum 0 likhte nh hai lakin ye 0 se he uthata hai same answer

print(a3[3 : 5 , 4 : 6]) # 3 to 4 tk ki rows and 4 to 5 tk k coloumn

#====================Skipping slicing=================>>
a4 = np.arange(0 , 36).reshape(6 , 6)
print(a4)
print(a4[2 : 5 :2 , 1 : 4 : 2]) #2 se lekr 5 tk ki row tk ka data lao or 1 skip krdo | 1st coloum se uthao 3 coloum tk or 1 skip krdo

print(a4)
print(a4[2 : 5 , 2 :6]) #practice
print(a4[0:5:2 ,  0 : 5 : 2]) #practice


#==========================3D=========>>

a5 = np.arange(1 , 13).reshape(3 , 2 , 2)
print(a5)
# print(a5[2 , 0 : 2 , 1]) #depth ,  rows , coloum
# print(a5[0:3 , 1 , 0 : 3]) # depth rows , coloum
# print(a5[0:3:2 , 0 , 0:2 ])

#======================nditer========>>

a6 = np.arange(1 , 13).reshape(3 , 2 , 2)
for n in np.nditer(a6):
    print(n) #Aab single number milega

#====================Transpose===========>
print(a6)
print(np.transpose(a6))#rows coloum ban jayegi
print(a6.T) #same kaam

#==========================Raval ================>>
#ye original me change krega

ar7 =  np.arange(1 , 13).reshape(3 , 2 , 2)
convert = np.ravel(ar7) # ye 1D me convert krdega 
convert[0 : 2] = 350
print(convert)

#===================Flatin============>>

#flatitn actuall copy bana raha hai jo hame original wali aray me change dkhne ko nh milega ravel ulat hai wo original me change krega


#=============================Stacking================>>
arr7 = np.arange(1 , 5).reshape(2,2)
arr8 = np.arange(6 , 12).reshape(2 , 3)
print(np.hstack((arr7 , arr8))) #combine kr k ans dedega horizontal stake krdega


#====================vstack==========

arr9 = np.arange(6 , 12).reshape(3 , 2)
arr10 = np.arange(1 , 5).reshape(2,2)
print(np.vstack((arr9 , arr10))) #vertically stack krwadega










