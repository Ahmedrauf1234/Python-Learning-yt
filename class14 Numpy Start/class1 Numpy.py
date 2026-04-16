#================================Numpy Intoduction====================>>
#numpy library hai python ki list se 10times faster hai or ye c language me likhi gai hai.. lakin is k opoer  syntax ki layer hena wo python ki hai sari execution c language me hoti hai
#numpy dikhti list ki tarah hai lakin list se bilkul diffrent hai opeation wise har tarah k operations perform krsakhte
#numpy ko used krte hve dosri libraries ko desgin kra gaya hai jaise pandas hai
#python wali list isnliye slow hai q k usme har datatype store krsakhte hen lakin numpy me aisa nh hota 1 he dataype store krni pari agar int or float hnge to numpy sab ko float banadega
# maths k saare functions dekhne ko milenge statistics wagra ML k
# fixed size hota hai same data type contain krti hai faster hai or other libraries me ye cheez used horahi hoti

#========================creating array================>>
#1 D arrray me numpy rows and coloum consider nh krta 2D se consider krna shuru hota hai

import numpy as np
#====================1D Array=========>>
arr1 = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])
print(arr1)
print(type(arr1)) 
print(arr1.ndim) #1st demention arry isko vector bolte hen

#==========2D Array=========>>

arr2 = np.array([[1, 2 , 3 , 4]])
print(arr2.ndim) # ye dimention batata hai
print(arr2.shape) #or ye kitni rows hen or kitne coloum hen wo batata hai

arr3 = np.array([[1,9] , [2 , 10]])
print(arr3)
print(arr3.ndim) #2 D array
print(arr3.shape) # (2, 2) 2 row 2 coloum

#==================create a 3 x 4 array 2D array==========>>

arr4 = np.array([[1 , 2 , 3 , 4] , [5 , 6 , 7 , 8] , [9 , 10 , 11 , 12]])
print(arr4.shape) # 3 rows 4 coloum
print(arr4.ndim) #2D Array

#=================3D Array=======>>
#[[[]]] 3d array

arry5 = np.array([[[4 , 5]]])
print(arry5.ndim) # 3 Dimention
print(arry5.shape) #(1 , 1 , 2) 1 depth 1 row 2 coloum

arry6 = np.array([[[4 , 5]] , [[6 , 19]]])
print(arry6) # 2 rows 2 coloum
print(arry6.ndim) #3D Array
print(arry6.shape) #(2 , 1 , 2)

arry7 = np.array([[[4 , 5],[3 , 7]] , [[6 , 19], [12, 56]]])
print(arry7)
print(arry7.shape) #(2 , 2 , 2)




#=================Dtype=========>>!!1


print(arry7.dtype)

arr8 = np.array([1 , 5.9 , 7.8 , 8 , 0 , 3.8])
print(arr8) # 2 datatype ko 1 datatype me convert krdiya float me string me kam nh krti sirf numeric data per kam krti or dtype datatypw batata hai

#=================Arrange============>>

arr9 = np.arange(11 ,50)
print(arr9) # 11 se 49 tk k numbers leke ajayega akhri wala include nh hoga

#================Reshape==========>>

R1 = np.arange(1 , 21).reshape(2 , 10) #2 rows 10 coloum
print(R1)

R2 = np.arange(1 , 28).reshape(3 , 9) #3rows 9 coloum
print(R2)

#===============np.ones================>>

R3 = np.ones((4 , 9)) #ones means 4 row 9 colum tk ones laake dedega float meleke ayega
print(R3)

#===============np.zeros================>>

R4 = np.zeros((4 , 9)) #zeros means 4 row 9 colum tk ones laake dedega float me leke ayega
print(R4)

#===============np.random================>>
R5 = np.random.random((4 , 9))*100
print(R5) #float me dega ramdom numbers

#aagr integer me chaiye hn

R6 = np.random.randint(-300 , 300 , 20).reshape(4 , 5) #-300 se leke 300 me se only 20 numbers leke aao
print(R6)

#================Linspace means linear space=============>>
R7 = np.linspace(3 , 15 , 5) 
print(R7) # 3 se 15 tk num leke ayega  or 5 num leke ayega barabr kr k ye numbers ko is tareeqe se leke ata hai un k darmiyan diffrence same rehta hai

#===============np.identity===========>>

a1 = np.identity(5) # means 5 rows 5 coloum or 5 dafa 1 leke ayega
print(a1)

#==============================
a2 = np.arange(1 , 28).reshape(3 , 3, 3)
print(a2)