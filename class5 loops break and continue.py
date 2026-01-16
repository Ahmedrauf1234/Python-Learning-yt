#==============================Loops==============================>>!!

#jo kaam hame bar bar krwana ho to hum loop ka used krte hen
#while ---> jab tk ---> condition --> ye con sahi rehti hai --->> tab tk kaam krte raho

# count = 0 #isko iterators kehte hen
# while count <= 5:
#     print("Ahmed" , count)
#     count += 1 #loop k chakkar ko iteration kehte  hen

    #=====================practice questions for while loop=====================>>!!

    # i =  1
    # user = int(input("Enter number?"))
    # while i <= 10:
    #     print(f"{user} x {i} = {user*i}")
    #     i += 1
        
#=======================================

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# idx = 0
# while idx < len(numbers): #isko bolte hen traverse krna means list k oper travel krna
#     print(numbers[idx])
#     idx += 1

#==================================>>
# nums = (1, 2, 3, 4,11, 5, 6, 7, 8, 9, 10 , 11)

# i = 0
# x = 11
# while i < len(nums):
#  if (nums[i] == x): #isko linear search bolte hen
#     print("yes match" ,i)
#     break     
#  else:
#    print("finding...")
#  i += 1

 #=================================Break ====================>>!!

# num1 = 0

# while num1 < 10:
#   if (num1 == 5):
#     print("match" , num1)
#     break # jaise he nisko 5 milega ye lopp break kr k bahar ajayega us k baad aage ka loop nh chalega
#   else:
#     print("finding...")
#     num1 += 1

#=======================Continue===================>>

# j = 0

# while j <= 10:
#     if(j == 5):
#         print("5 mil gaya")
#         j+=1
#         continue # ye skip krne ka kaam krta hai 5 k elawa sab ajayega
#     print(j)
#     j += 1

#=================================For loop======================>>
# nums = (1, 2, 3, 4,11, 5, 6, 7, 8, 9, 10 , 11)

# for val in nums:
#     print(val)

# str = "Ahmed"
# for char in str:
#     print(char)
# else:
#     print("end") # ye isliye likha loop porana chalne k bad hame kuch print krwana ho to else likhte hen hum|| agar break laga hota condition k saaath  to elase nh chalta

#===========================practice question for loop==============>>

# numbers_1 = (10, 20, 10, 30, 40, 20, 50 , 70 , 50 , 50, 67 )
# check = 50
# index = 0

# for el in numbers_1:
#     if( el == check):
#         print("Matched at index " , index)
#     index += 1


#+==============================range in for loop==================>>!!

# for seq in range(0 , 10):
#     print(seq)

# for seq in range(10): #only stop point kehleyaga means 0 se 9 tk chalega
#     print(seq)

# for seq in range(2 , 10): #start or end diya hva 2 se 9 chalega
#     print(seq)

# for seqs in range(0 , 100 , 2): #startv end and skip 
#     print(seqs)

#================================practice queatins===============>>!!

# for n in range(100 , 1 , -1):
#     print(n)     

# user = int(input("Enter number?"))
# for n in range(1 , 11):
#     if(user == ""):
#         print("write a number")
#     else:
#         print(f"{user} x {n} = {user*n} ")

#=========================Pass in loop========================>>!!


# for skip in range(0 , 10):
#     pass   # pass isliye used hota kli loop hame khali chorna hai means abhi isnme kaam nh krna pass likhe begair hum khali chordenge to aage ka code run nh krega is wajah se pass likhte hen

    
#==============================

n = 5
sum = 0
for i in range(1 , n+1):
    sum += i
    print(sum)

 