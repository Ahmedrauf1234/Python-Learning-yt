#===============================================Encapsulation============================>>
#Encapsulation means aap ko jo data apne tk rakhna user ko nh dikahana to aap data ko encapsulate krsakte ho

class Person:
    def __init__(self , name , country):
        self.__name = name   #__name isse data secure hojayega class k andar ascess hojayega lakin bahar nh hoga
        self.__country = country
    #getter method
    def show_name(self): #class me reh k data ko ascess ese krenge method bana k next show name ko bhi hide krdiya __show_name()
        return print(self.__name)
    #setter method
    def change_name(self , new_name):
        self.__name = new_name

    

p3 = Person("Anas" , "Pakistan")
# print(p3.__name) #error ayega name show nh krega
p3.show_name() #ab ascess krsakhte hen 
p4 = Person("Ahmed" , "lahore")
# print(p4._Person__name) #hide hvi vi cheeez ko bhi ascess krsakhte asal me python hide nh krta us varible ka name change krdeta hai professionally sahi nh hai ye getter or setter used hota || or hum value bhi change krsakhte name mangling kehlata
# p4.__show_name() #error 

# p4.show_name()
p4.change_name("Talha")
p4.show_name()
#===========================
sp1 = Person("alishba" , "Ahmed")
sp2 = Person("umama" , "hammad")
sp3 = Person("Hassan" , "Ahmed")

persons = [sp1 , sp2 , sp3]
print(persons[0]._Person__name) #isko list me rakh k bhi hum name acsess krsakhte hen

for person in persons:
    print(person._Person__name) #loop bhi chala sakhte

persons_data ={
    "per1" : sp1,
    "per2" : sp2,
    "per3" : sp3

}
print(persons_data["per1"]._Person__name) #dict se bhi data ascess krsakhte


#============================= Static Varibles =====================>>

# jo hum class k andar varible likhe  jaise cid isko static varibles kehte hen ye class level per kam krte hen har obj k liye fix hote hen class me likh k constructor me handle krte
#static varibe class k andar or constructor k bahar likha hva hai to wo same rehta hai sab k liye
#intense varible wo hota jo fix mhi ho ahr bar change horha ho jaise costumer ka name 
#bank ka iban number har costumer k liye 1 jaisa hota to wo static kehlata hai kabhi change nh hota
class Atm :
    cid = 1 #ye class ki id hai constructor ki nh hau isko neachsy Atm.cid kr k aqcess krenge
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.cid = Atm.cid #hum
        Atm.cid += 1

#==============================Aggregation==========================>>

class Costumer:
     def __init__(self , name , age , cell , cnic , address):
         self.name = name
         self.age = age
         self.cell = cell
         self.address = address
         self.cnic = cnic

     def show_details(self):
         return print(f"Costumer name is {self.name} and age is {self.age}, and address is {self.address.state} ")
     
     def show_address(self):
         print(self.address.hno)
         print(self.address.street)
         print(self.address.block)
         print(self.address.state)
         print(self.address.city)
    
     def change_state_city(self , state , city):
         self.address.change_details(state , city)
        # self.state = state
        # self.city = city
     
class Address:   #user ka address alag se class bana k rakhte hen
    def __init__(self , Hno , street ,state, block , city):
        self.hno = Hno
        self.street = street
        self.block = block
        self.city = city
        self.state = state

    def change_details(self , state , city):
        self.state = state
        self.city = city

    
    

        
     
a1 = Address(1142 , 125 , "sindh" , "D" , "karchi")
c1 = Costumer("Ahmed" , 24 , 2234556 , 2898938798792 , a1 )
c1.change_state_city("punjab" , "lahore")
c1.show_address()
    
         







