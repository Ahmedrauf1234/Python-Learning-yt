#===============================Functions python==========================>>
# function ko used isliye krte hen take hamare code me reduntancy kam hojaye
# jo code hame bar bar likhna hai usko hum 1 fuction me likh dete hen 
#jo function hum khud likhte hen usse user define kehte hen || or jo pythion k apne hote hen use built in kehte hen

def calc(a , b): # paramerter
    sum = a + b
    print(sum)
calc(5 , 6) #arguments

def print_hello():
    print("Hello!!")
    
    
output = print_hello()
print(output) #none 


#==========================
def mul_pro(a = 1, b = 2):
    print(a * b)
    return a * b
mul_pro() #yhn error ayega arguments pass nh kre|| error ko hatane k liye hum parapeter me default value desakhte hen | hum 1 value bhi pass krsakhte or 1 arguments me dedete


#==========================Practice questions==================>>
words = ["apple", "book", "cat", "dog", "earth", "flower", "green", "house", "ice", "juice"]

def len_list(list):
    print(len(list))
# len_list(words)
#=====================
list1 = ["pen", "pencil", "eraser", "notebook", "marker", "sharpener", "ruler", "bag", "desk", "chair"]

def print_list(list):
    for items in list:
        print(items , end=" ") #end 1 he line me le ayega
# print_list(list1)

#=================================


def print_fact(n):
    fact = 1
    for i in range(1 , n+1):
      fact *= i
    print(fact)
# print_fact(6)

#=================================

# user_inp = int(input("Enter Amount?"))
def converter(Dollar_Val):
    pak_Val = Dollar_Val * 279.98
    print(f"dollar Val {Dollar_Val} Converted into PKR {pak_Val} ")
# converter(5)
#===============================

def Check_Num(num):
    if(num % 2 == 0):
        print("This is even Number")
    else:
        print("This id Odd")
# Check_Num(2)
#===============================

#=============================Recursion in python=======================>>!!

#Recursion loop ka he 1 version hai
#jo kaam hum loops se krte hen wo recursion se bhi kiya jaa sakhte
#sab se pehle recurion me hame kaam batana hota hai or condition zarori hai

# def show(n):
#     if(n == 11): # isko base case bolte hen means stopping condition
#         return
#     print(n)
#     show(n+1)
    # print("end")
#show(1) # 1 se lekar 10 tk counting print krdega

#====================Example Recursion factorial=================>>
# def cal_fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return cal_fact(n - 1) * n
        
# print(cal_fact(4))

#=======================Recursion practice questions===============>>!!
# def nat_Num(n):
#     if(n == 0):
#         return 0
#     else:
        
#        return nat_Num(n - 1) + n

# print(nat_Num(10))

#=============================

# cars = ["car", "bus", "train", "bike", "plane", "ship", "truck", "van", "scooter", "metro"]
# def print_list(list , idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list , idx+1)
# print_list(cars)

#===========================Enumirated==================>>

# cars = ["car", "bus", "train", "bike", "plane", "ship", "truck", "van", "scooter", "metro"]

# for index, car in enumerate(cars):
#     print(index , car) #ye hame index or value dono lake deta hai

#=========================Quiz function==============>>!!


quiz = [
    {
        "question": "Python kis type ki language hai?",
        "options": ["Compiled", "Interpreted", "Machine", "Assembly"],
        "answer": "B"
    },
    {
        "question": "Python me list ka symbol kya hota hai?",
        "options": ["()", "{}", "[]", "<>"],
        "answer": "C"
    },
    {
        "question": "Python me output ke liye konsa function use hota hai?",
        "options": ["print()", "show()", "display()", "output()"],
        "answer": "A"
    },
    {
        "question": "Python me comment kis se hota hai?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "B"
    },
    {
        "question": "Python me keyword ka rang IDE me kaisa hota hai?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": "B"
    }
]

def quizapp():
   Score = 0
   for index, ques in enumerate(quiz ,start=1):
       print(f"Q{index} {ques['question']}")
       for option in ques["options"]:
        print(option)
        
        
       user_input = input("Enter Anwer: ABCD?").lower().strip()
       if (user_input == ques["answer"].lower()):
            print(f"Correct Answer!!")
            Score += 1
            
       else:
            print(f"Wrong Answer!! correct is {ques['answer']}")
        

   print("Quiz finished")
   print(f"your score is {Score}")
        
    
    
    
    
        


# quizapp()
#===========================task questions==============>

