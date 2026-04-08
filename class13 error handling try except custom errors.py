#============================Errors types and error handeling===============>>


# ===================1 ) module not found error===============

# import mathyyy #math ki spell ghtl error ayega #module not found error


# =====================2)key error=================

d = {
    "name" : "Saylani"
}
# d["age"] # error age name ki koi key nh hai to key error


# =====================3) type Error======================

# num1 = float(input("type number 1"))
# num2 = input("type number 2")
# print(num1 + num2) # type error num2 ko float me convert nh kra difrent type ki data type ko sum krna chahye nh krerga kaam

# 4) ======================Value error==================

# int("abc") #value error ghlt cheez ko type cast krrahe

# ===================5)  Name Error==================

name = "Saylani"
# print(names) # name error jo hum print krrahe wo exists nh krta
# print(a) # name error a name ka varible kahi banaya he nhi a is not defined

# ================6) Attribute error================

name1 = "Saylani"
# name1.append('s') #attribute error q l append list ka method hai

#=======================================Err Handeling Try except===================???
 

# try:
#     with open('errorfile.text' , 'r') as f:
#         print(f.read())
#         # print(5 + "66") #oper wali 2 lines chal rahi hogi agar 3rd line me err hoga phr bhi file not found shor krdega jo err arha hota usse related msg show krwana hota hai
# except:
#     print("file not found")
#=============================== Handeling err=================


# try:
#     with open('D:\Python Course youtube\class7 demo.txt' , 'r') as f:
#         print(f.read())
#         # print(5 + "69") #err
#         print(5 + 5) # ye execute nh hoga q k oper err hai 

# except FileNotFoundError: #1 err handle hogaya
#     print("file not found")

# except TypeError:
#     print("Wrong data Type")

#============================shortcut of err handeling==============>>
# bht sare errs aane ka chances hote hen to bari bari beth k to handle nh krenge


try:
    with open('D:\Python Course youtube\class7 demo.txt' , 'r') as f:
        print(f.read())
        print(5 + "69") #err
        print(5 + 5) 

except Exception as e: #1 err handle hogaya
    # print(e) # jo err ayega wo handle hojayega err ka right wala parh shoe hojayega
    print(e.with_traceback) # iise err ka left parh milega err ki type batayyega

#=========================
#else tab kam krega jab oper wala koi bhi except kam nhi krega
#finally compulsary hai
#try expet multiple hosakhte hen lakin else finally 1 hoga 
#finally k andar hum aisa code likh sakhte jo hame lazi chalani hai execute krni hai wrna finally ka itna kam nh hai

try:
    file = open('D:\Python Course youtube\class7 demo.txt' , 'r')
        # print(f.read())
        # print(5 + "69") #err
        

except FileNotFoundError: #1 err handle hogaya
    print("file not found")

except TypeError:
    print("Wrong data Type")

else:
    print("In the else")
    print(file.read())
finally:
    print("hamehsa chalega kuch bhi hojaye") #finally chalega he chalega  abhi yhn else chal rha hai q k except wnh chal rha 


#=========================Raise Exception===================>>
# ese hum apne arrers bana sakhte hen Name err ki jagah per hamara ye wala msg print krwadega
#builtin errs ko hum apne alfaz me define kr sakhte hen
#jo err hame show krna ho to ese kr sakhte hen

# raise NameError('Bhai' , 'varible nh mil rha')

#========================================Creating Custom Exceptions==================>>
class MyException(Exception):
    def __init__(self, msg):
        # print(msg)
        self.msg = msg

class bank:
    def __init__(self , balance):
        self.balance =  balance

    def withdraw(self , amt):
        if amt < 0:
            raise MyException("Negative ammount kese nikaloge")
        if self.balance < 0:
            raise MyException("Itne paise account me nh hai")
        
b1 = bank(1000)
# b1.withdraw(-50000)

try:
    b1.withdraw(-50000)
except MyException:
    print("bhai paise negaive nh hosakhte")
        

        



