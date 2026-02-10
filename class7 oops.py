##===============OOPS IN PYTHON (object orenting programming))====================>>
#functionn ko used krte hve redundancy reduce hojati hai reuseability increase hojati hai

class Student:  #ye class hai
    name = "Ahmed"

# s1 = Student()  #ye object hai
# print(s1.name)

# class Car:
#     color = "Blue"
#     model = 2004
#     brand = "Honda"
# car1 = Car() #ye object ahai
# print(car1.color)
# print(car1.model , car1.brand)

#===============================COnstructor====================>>
#self 1 refrence hai to the current instance of the class and it used to acess varibles that belong to the class
#ye default per parameter leta hai self naam ka ye hamesha 1st hota hai us k bad multiple parameter le sakhte
#jo data class k andar hum store krte hen usko hum intance attributes kehte hen
#agr hum class k andar constructor nh likhte python usko default per bana dena or print ki jagah per pass krdeta
#object attribute bara hota hai class attrribute se
#object value or class value dono sab hota to object value ko zada value di jati wse ye used nh hota itna
#constructor basically object k initiallization k liye hota hai mtlb ap obtect ko ctreate krte time kuch kam krwana chahte hen jaise hum attributes add krna chahte hen wo kam hum constructor k zarye krte hen

class Students : #this is class
    college_name = "Abc College" #college to sab ka samne hoga to ye class k andar 1 dafa likha
    name = "Anonymous" #class attributes 
    
    
    def __init__(self , fullName , marks): #ye parameter wised constructor hai wo parameter jis k andar self k elawa bhi parameter ho
        
        self.name = fullName #self. ka mtlb hai har object ka name alag hoga marks alag hnge ye object attributes kehlata hai
        
        self.marks = marks
        print("Adding new student in Database")


# s2 = Students("Talha" , 88) #this is object
# print(s2.name , s2.marks)
# s3 = Students("Muahmmad" , 67)
# print(s3.name , s2.marks)
# print(s3.college_name)
# print(Students.college_name) #same ans
# print(s3.name)



#================================ Methods====================>>
#class k andar 2 cheezien store hosakhte (DATA means Attributres, methods means (jo function class mee likhe jate use hum methods keh dete))
# class k andar jab bhi hum funtion likhte hen us ka bhi 1st parameter self likhteb hum
# 2 atreeqe k attributes hote hen class or object attribute


class Students1 : #this is class 
    college_name = "ABCD COLLEGE" #ye class attributes he

    def __init__(self , name , marks):#this is constructor ||
        self.name = name #ye bobject attribues heen
        self.marks = marks
    
    def welcome(self): #class k andar welcome function
        print("Welcome Student" , self.name)
    
    def get_marks(self):
        # print(f"marks is {self.marks}")
        return self.marks

# s = Students1("Ayesha" , 99)
# s.welcome()
# print(s.get_marks())

#==========================Task And static mrthod @static method================>>

class Students3:
    def __init__(self , name  , marks):
        self.name = name
        self.marks = marks

    def get_avarage(self):
        sum = 0
        for index, items in enumerate(self.marks , start=1):
            print(f"subject is {index} marks is {items}")
            sum += items
        avg = sum / len(self.marks)
        print(f"{self.name} and your avrage score is {avg}")

#=====================Statis method concept ================>>
    @staticmethod #isko decorator bolte hen ye function ka behavior change krdeta hai
    def hello(): #self nh likhenge err ayega lakin yhn self ka kam nh hai q likhen? err se bachne kliye @staticmethod likhenge to err nh ayega
        print("Hello")

s10 = Students3("Ahmed" ,  [90,34, 66])
# s10.get_avarage()
s10.hello()



#=================inportant consepts of oops Abstraction and Encapsulation==========>>


# class Car :
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def Start()




    









