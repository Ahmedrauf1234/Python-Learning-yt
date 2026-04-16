import numpy as np

#=============================Bits and Bytes Concept=================>>!!
arr1 = np.arange(-11 , 12)


arr2 = arr1.astype(np.int16)
print(arr2.dtype)
arr3 = arr1.astype(np.float16)
print(arr3)
print(arr1.shape) #agr 1 demention array hen to wo total num of items batata hai

#===================
#rowa and coloum tab exists krte hen jab hamare pass 2d ya 2d se oper ki dimentions hn agar 1d hai to wo usko vector consider krrha hota hai
# ye sab attributes hen

arr4 = np.arange(1 , 26).reshape(5 , 5)
print(arr4)
print(arr4.ndim) # 2 dimension
print(arr4.shape) #(5 , 5) 5 row 5 coloum
print(arr4.size) #ye array me kitne items hen wo batata hai
print(arr4.itemsize) # ye bytes batata hai k kitni bits ka data hai lakin batata bytes me hai 8 bytes means 64 bits



#===========================Array Operations==================>>

arr5 = np.random.randint(1 , 20 , 8 ) #1 se lekr 5 tk num genrate kro lakin lake 2 num do
print(arr5)
mulArr = arr5 * 5 #pori array per operation perform krega har item per
print(mulArr)
print(arr5 > 10 ) #true false me ans ayega sab items per jakr check krega


arr6 = np.arange(1 , 11)
arr7 = np.arange(11 , 21)
print(arr6 + arr7) # dono ko sun krdega
print(np.max(arr7)) # sab se bara num leke ayega
print(np.min(arr7)) #sab se chota num leke ayega
print(np.sum(arr7)) #pori array ko sum krcega
print(np.prod(arr7)) #pori array ko multuply krdega

#=========================== Row and coloum wise operations===================>>

#axis =========== 0 ====coloum
#axis ========= 1=======Row

a1 = np.arange(1 , 26).reshape(5 , 5)
print(a1)
print(np.max(a1 , axis=0)) # sab k coloums wise number lake dega [21 22 23 24 25]
print(np.max(a1 , axis=1)) # sab k row wise number lake dega [ 5 10 15 20 25]


#========================Aggregate Functions===================>>
#mean
# median
#mode ---> no direct method
#std
#var
#-------------------Mean===============
a2 = np.arange(1 , 11)
print(a2)
print(np.mean(a2)) # 1 se 10 tk k numbers ko plus krega or array ki length se devive krdega data ka center point batata hai ye

#-------------------Median===============

print(np.median(a2)) # ye odd quantity k numbers ka beech wala num leke ayega 1 se 10 tk print krwaye num 1 se 4 6 se 10 beech me bacha 5 ye wo laake dedega
print(np.median(a2)) # ab odd nh hai to 1 se 4 or 7 se 10 beech me bache  5,6 dono ko plus kr 2 se divide krdega to ans 5.5 ayega


#=========================Mode================>>
# jo number array me bar bar repeaat hota hai mode wo numbers laake dikha raha hota hai

a3 = np.random.randint(1 , 6 , 8)
print(a3) #ab ye kuch numbers repeat krega [4 5 4 1 1 3 2 4]
data , count = np.unique(a3 , return_counts=True) #isko true krne se count bhi mil jayenge
print(data) #yhn per data ayega unique numbers ayehnge jo repeat nh hva [1 2 3 4 5]
print(count) # or yhn per count ayega 1 numbers kitni dafa repeat hva hai [2 1 1 3 1]

# print(np.argmax(count)) #ye count me jo sab se bara number hena us ka index dega || np.max hame actuall data laake deta tha na ye data nh index laake dega
print(data[np.argmax(count)])

#==================


