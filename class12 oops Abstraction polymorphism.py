#=================================Polymorphism  3 types=====================>>
# 1) method overriding #ye parh chuke paranrt me bhi method ho child me bhi ho child ka object bana k parant k method ko ascess nh krsakhte child ka chale
# 2) method overloading
# 3) operator overloading

#======================Method overloading (nh kam krti python me)==============

class Area : #constructor isliye nh bnaya q k hame neachey method me value used nh krni sab jagah alag alag values hen to faida nh constructor jab banate tab koi value hame saare methods me chaiye he chaiye hoti to 1 dafa constructor me likh k neachey used krte rehte

    def calc_area(self , radius , pi = 3.142):
         return pi * (radius * radius)
    
    def calc_area(self ,  length , bredth): #ye method over loading hai sab se akhri chalega method ka name same hoga 
         return length * bredth

# a1 = Area()
# print(a1.calc_area(3 , 6))

#===========================Methid Overloading============

class Area :
     def calc_area(self , a , b = 0):
          if b == 0:
               return 3.142 * a * a
          else:
               return a * b
          
# a2 = Area()
# print(a2.calc_area(2))

#==============================Operator overloading=====================>>

#operator overloading python me supported hai lakin method overloading pyhton me supported nh hai
#  

#================================Abtraction ========================>>!!

from abc import ABC , abstractmethod #from k bad abc fila ka name hai import ABC class ka name hota abstractmethod us file me method ban k rakha hva hai jo hum ne bolaliya

class bankApp(ABC):
     
     def database(sself):
          print("conntected to database")

     @abstractmethod    # means mere security wale mathod ko compalsury banado agr child bankapp ko inherit krha hai or us k pass security nh hai to wo inhert nh krsakega
     def security(self):
          pass
     
class MobileApp(bankApp):
     
     def login(self):
          print("login Sucessfull.")

     def security(self):
          pass

ma1 = MobileApp()
# ma1.security() #error
# ma1.login() err #ye bhi nh chalega jab tk child me security ka method nh likhenge
# ma1.database() # chalega q k security child me hai
    
          
     
    

    

    
