#=========================================Saylani concepts oops class 1=======================>>


class Atm :

    def __init__(self):
        self.pin = None
        self.balance = None
        # print("inside constructor")

    def create_pin(self):
        pin = input("type your pin")   #is digit jab kam krega jab usko string k andat integer value milegi means number
        if pin.isdigit():
            self.pin = pin
            print("print is set sucessfully")
            amount = input("Enter Your Amount want to deposit")
            if type(float(amount)) == float:
                self.balance = float(amount)
            else:
                print("please enter the correct amount")
        else:
            print("pin is not correct")
    

    def change_pin(self):
        old_pin = input("type old pin : ")
        if old_pin == self.pin :
            new_pin = input("type new pin : ")
            self.pin = new_pin
            print("new pin set sucessfully")
        else:
            print("pin incorrect")

    def deposit_amount(self):
        pin = input("enter your pin : ")
        if self.pin == pin:
            amt = float(input("enter amount"))
            self.balance += amt
            print("amount saved sucessfully")
        else:
            print("pin incorrect")
    

    def withdraw_amt(self):
        pin = input("enter your pin : ")
        if self.pin == pin:
            amt = float(input("enter withdraw amount :"))
            if self.balance >= amt:
                self.balance -= amt
                print(f"withdraw sucessfully and remaining bal is f{self.balance}")
            else :
                print("your balance is in insufficient")
        
        else:
            print("pin incorrect")




# u1 = Atm()
# u1.create_pin()
# # print(u1.balance)
# u1.deposit_amount()
# u1.withdraw_amt()


#=====================================Fraction and point  Class using= OOP Class 2====================>>

class Fraction:

    def __init__(self , numi , denom): #hum contructor me self k elawa or perameters isliye likhte hen jo hame poori class me bar bar used krne hen numi or denom aage mujhe bar bar used krna hai isliye likha..constructor me 1 dafa likh do bar bar used krte raho
        self.numi = numi
        self.denom = denom
    
    def __str__(self):  #__str__ ye 1 megicial method hai python ka || megical method khud call hote hen krna nh parta
        return f"{self.numi}/{self.denom}" #str method display krwane k liye hota bs division laga hva mtlb sirf disvision k sath display krwayega
    
    def __add__(self, other):
        num = self.numi * other.denom + other.numi * self.denom
        den = self.denom * other.denom
        return f"{num} / {den}"
    
    
    def __sub__(self, other):
        num = self.numi * other.denom - other.numi * self.denom
        den = self.denom * other.denom
        return f"{num} / {den}"
    
    def __mul__(self, other):
        num = self.numi * other.numi
        den = self.denom * other.denom
        return f"{num} / {den}"
    

    def __truediv__(self, other):
        num = self.numi * other.denom
        den = self.denom * other.numi
        return f"{num} / {den}"

        

# f1 = Fraction(3 , 4)
# f2 = Fraction(6 , 11)
# print(f1 * f2)


#====================================== questions Solving================>>

class Point:
    
    def __init__(self , x , y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x} , {self.y})" #ye sirf display k liye hai operation perform krne k liye nh hai
    
    def calc_distance(self , sp): #distance ka for lagaya (x2-x1)**2 + (y2-y1)**2 hole per root
       distance = ((sp.x - self.x)**2 + (sp.y - self.y)**2)**(1/2)  #root ki value 1/2 hoti
    #    print(distance)
       return distance
    
    def calculate_distance_from_origin(self):
       return self.calc_distance(Point(0,0))  #oper wale calc_distance ko neachey call kra hai
    



p1 = Point( 10 , 2)
p2 = Point( 12 , 2)

print(p1.calculate_distance_from_origin())


class Line: # Q is kiya user ka point line per lie krta ya nh? 
    def __init__(self , a , b , c):  #ax + by + c = 0 is formula se check krrahe
        self.a = a
        self.b = b
        self.c = c
    
    def point_on_line(self , point):
        if self.a * point.x + self.b * point.y + self.c == 0:
            return print( "point lies on the line")
        else:
            return print("point is not lies on the line")
    
    def distance_from_line(self , point): #d = |Ax1 + By1 + c / A2 + B2 ** 1/2 means root hai 
        return abs( self.a * point.x + self.b * point.y + self.c) / (self.a**2 + self.b**2) ** 0.5


l1 = Line(5 , 7 , 9) #2x + 3y + 4 = 0 yhn tk ye ban rahi equation
# l1.point_on_line(p1) #2(3) + 3(4) + 4 = 0 or yhn per ye eq ban rahi 
l1.distance_from_line(p1)  

