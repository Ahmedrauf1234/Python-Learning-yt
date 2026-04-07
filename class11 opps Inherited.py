#====================================Inheritance======================>>!!
#cihild class me contructor ko inherit krsakhte -- non private methods -- non private attributes aise attributes jo diuble __ k sath nh likhe hve
#agar parant me constructor majood hai or child me bhi majood hai or child me parant wale constructor ko inherit kiya hva hai or execute child ko kra to child wala constructor chalega parant wala nhi. bahle hamne inherit kiya hva ho. agar child me constructor nh hai sirf parant me hai to phr parant ka chalega q k sonstructor megical hai chalta he chalta hai or child wala constructor ka object bana k child wali values pass kr lakin print parant ka values krwayenge to err ayega lakin method chal jayega jo paranr me hai jo alag se function banaya hai child k pass or koi function nh hia jabhi parant wala function ko chaladega

class User :
    def __init__(self):
        self.name = "Muhammad Ahmed"
    
    def login(self):
        print("Login Sucessfull")

class Student(User): #parant wali class ko child class me inherit kiya hva hau || parant wali sari functionaility child em agai hai

    def enroll(self):
        print("Enroll into a course")

# u = User()
# s = Student()
# print(s.name)
# s.enroll()
# s.login()

#===============================Non private attribute======================>>
#agar non private attribute hva jabhi wo inherit hosakega means public attribute hva jabhi inherit hoga pprivate hva attribute parant k andar  to nh hoga inherit
class Phone:
    def __init__(self , price , brand , camera ):
        print("Inside the constructor")
        self.__price = price #is ka name change kr k python ne _Phone__price rakhdiya hai
        self.brand = brand
        self.camera = camera
    
    def show_price(self):
        print(self.__price) #ye axcess hoga q k class me reh k mathod banaya hai price show hogi lakin

class SmartPhone(Phone):

    def check_price(self):
        print(self.__price) #lakin yhn nh hogi q k hum child class me hai class k andar reh k axcess hogi lakin class k bahr nh isliye error


# s = SmartPhone(34000 , "Samsung" , "80MP")
# # print(s.brand)
# # print(s.__price) # error no excess private in parant
# s.show_price() #34000
# s.check_price() #error q k private hai 


#=====================Non private Methods======================>>


class Phone:
    def __init__(self , price , brand , camera ):
        print("Inside the constructor")
        self.__price = price #is ka name change kr k python ne _Phone__price rakhdiya hai
        self.brand = brand
        self.camera = camera
    
    def show_price(self):
        print(self.__price)
    
    def __show_brand(self):
        return self.brand
    
    class SmartPhone(Phone):
        def check(self):
            print(self.__price)
    

    s = SmartPhone(34000 , "iphone" , "120MP")

    s.show_price() #execute 34000
    # s.show_brand() #err this is private

    #================================Practice===============>>>

class Parant :
     def __init__(self , num):
         self.__num = num

     def get_num(self , num): #ye getter method kehlata hai
         return self.__num

class Child(Parant):

    def __init__(self, val , num):
        self.__val = val

    def get_val(self): #getter method
        return self.__val
        
son = Child(100 , 250)
# print("Parant Num : " , son.get_num()) #son.get_num ko son axcess kr parha hau inherit ki wajah se lakin value nh arahi
print("Child Num : " , son.get_val()) #execute Child Num :  100


#========================== paraant or child dono ka contructor call krwana ho=========>>

class User :

    def __init__(self):
        self.name = "Muhammaad Ahmed"

    def login(self):
        print('Login sucessfully')


class Student(User):
    
    def __init__(self):
        self.rollno = 1234
        super().__init__() #super se oper wali class user ko msg jayega or wo dono ko chaldega || ye yhn isliye likha hai q k hame user ko excess nh dena

    def enroll(self):
        print("enroll course")
    
    # u = User()
s1 = Student()
print(s1.name) #err nh ayega q k super ki madad se oper wale constructor ko axcess kiya


#==========================

class Phone:
    def __init__(self , price , brand , camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    # def show_price(self):
    #    return print(self.__price)

    def buy(self):
        print("Purchasing a Phone")
    
class SmartPhone(Phone):
    def __init__(self , price , brand , camera , os , ram):
        print("isnside at top of smartphone constructor ")
        super().__init__(price , brand , camera) #constructor me he super ka call zada hota hai
        self.os = os
        self.ram = ram
        print("inside and in the smart phone constructor")

s = SmartPhone(23000 , "Apple" ,"45MP" , 4567 , 256)
# s.show_price()



        

        
    






    


        

