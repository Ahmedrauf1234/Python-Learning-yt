# builtin functions in string

# 1) Slicing

str = "Apna College"
# print(str[0:5])
# print(str[0:len(str)])
print(str[-4:-1])


# 2) endwith -- ye batayega k ap ki string is word per khtm hoti hai ya nh?
str1 = "i am studying python"
print(str1.endswith('on'))
print(str1.capitalize()) #ye 1st word capital krega
print(str1.replace("y" , "m")) #jhn jhn y hoga ye m se replace krdega
print(str1.find('am')) #ye g batadega k knse index per hai || pora word bhi batadga
print(str1.count('a')) #a kitni dafa aya hai string me batadega

#==========================================Ends string builtin functions============

#==================================practice question===================>>
# user = input('enter your name?')
# print(len(user))

dollar = "Ahmed$Rauf_$$"
print(dollar.count('$'))

#===================================End==============================>>
#condition Statement If else

age = 100

if(age >= 18):
    print("apply lisence")
elif(age <= 18):
    print("apply")
else:
    print("cant apply")

#nedted if
# user =int(input("enter your age")) 

# if(user >= 18):
#     lisence = input("have lisence?")
#     if(lisence == 'yes'):
#         print("conrats")
#     else:
#         print("No buy lisence")
# else:
#     print("cant drive")




#===========================practice questions====================>>


# check_Num = int(input("Enter number?"))
# if(check_Num % 2 == 0):
#     print("Even")
# else:
#     print("odd")

#===============

#=================================Notes================>>

str = "hello"
print(str[0]) #ye hum krsakhte hen acess 
str[0] = "y" # ye nh krsakhte q k ye immutable hai change nh krsakhte isko alag se varible me rakh k bhi nh krsakhte
# print(str) #error



   


