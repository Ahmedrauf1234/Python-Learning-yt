
#============================List Topic==========================>>
student = [23.43 , 67.43 , "Ahmed" , True , "umer" ]
print(student[2])
student[2] = "Ali" #yhn per hum list ko change krsakhte hen lakin string mr nh krsakhte q k string immutable hai or list mutable hai
print(student)

sli = student[0:4]
print(sli)


#=================================List Methods======================>>

list1 = [1,2,3,6,9,12]
list2 = [34 , 43, 89 , 66]
list1.append(4) #akhir me 1 add krdega
list1.sort() #ye sort krdega assending way me counting wise|| string me bhi krsakhte Abcd wise aajyega
list1.sort(reverse=True) #ab list desending order me sort hogai bare se chota
list1.insert(1 , 5) # ye 1 index per 5 add krdega
list1.pop(2) #2 index per jo bhi hoga delete krdega
list1.extend(list2) #ye 2 lists to 1 me le ayega
print(list1)


#===================================Tuples======================>>
#1 dafa tuple ban gaya ab usme kuch add or delete nh hosakhta ye immutable hai

tuple1 = (1 , 2 , 3 , 4)
print(tuple1[1])
#tuple1[2] = 10  #yhn errfor hai hum change nh krsakhte 1 k tuple immutable hai list or tuple me yahi farq hai major list change kr sakh'te lakin tuple nhi
 #===================================>>

tup = (1,) #ye lg touple raha hai lakin hai nh pyhton isko integer suppose krraha hai tuple krne k liye 1 k bad , lagana hoga
print(tup)
print(type(tup)) #type iski int ayegi

#=========================methods in tuple================>>
tuple1 = (1 , 2 , 3 , 4 , 5 , 5 , 56 , 5)
print(tuple1.index(2)) #ye hame batayega k 2 knse index per mujood hai searching ka kaam krraha hai
print(tuple1.count(5))


#========================practice questions================>>
# movies = []
# userMov1 = input("Enter favourite movie")
# userMov2 = input("Enter favourite movie")
# userMov3 = input("Enter favourite movie")
# movies.append(userMov1)
# movies.append(userMov2)
# movies.append(userMov3)
# print(movies)

#==============================@nd question===================>>
pal1 = [1,2,1]
pal2 = [1,2,1]
copyList = pal1.copy()
copyList.reverse()
print(copyList)
if(pal2 == copyList):
    print("palindrome")
else:
    print("not pakindrome")

#================================end==============>>
#===========================tuple practice====================>>


grades = ("A" , "B" , "C" , "A" , "A" )
print(grades.count("A"))

#========================

#+======================palindrome in string==============>>

user1 = input("enter a string")
user2 = input("enter a 2nd string")
if (user1.lower() == user2.lower()[::-1]):
   print("palindrome")
else:
   print("not palindrome")









