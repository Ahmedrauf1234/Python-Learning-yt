#================================File I/O===================>>
#open likh k 1st parameter me file ka path phr mode batana hai
#agar file exits nh kregi to python wo file create krdega
#better syntax with opern("demo.text" , "a") as f streamit ki tarah



# f = open("D:\Python Course youtube\class7 demo.txt" , "r") #ye read krta hai file ko
# data = f.read() #yhn argument deke number of caharacter bhi find krsakhte
# print(data)
# print(type(data))
# f.close()

# line1 = f.readline()
# print(line1)

#=============================Writing a file=========================>>
#ye file k andar ka data overwrite krdega "W"
#ye data append krdega "a"

# f = open("D:\Python Course youtube\class7 demo.txt" , "a")
# f.write("\n I want to run php tommorrow. Muhammad Ahmed")
# f.close()


#=========================R+ (read and over write krsakhte existing data ko) ===================>>
#file k start me abc laga dega overwrite krdega
#read mode me khol k write ki madad se overwrite krdiya

# f = open("D:\Python Course youtube\class7 demo.txt" , "r+") #this overwrite to ABC
# f.write("Abc")
# print(f.read())
# f.close()

# #=========================W+ (delete old data then add data) ===================>>
# #ye file ka data delete krdega jo rakh ahva  hoga pehle se us k abd ap dsata write krsakhte

# f = open("D:\Python Course youtube\class7 demo.txt" , "w+") 
# f.write("Muhammad Ahmed")
# f.read()
# f.close()


#+=============================A+(read and append data)=============================>>

# with open("D:\Python Course youtube\class7 demo.txt" , "a+") as f: #close lagana zarori nh with k sath
#     f.write("Helllo python\n")
#     f.seek(0) #ye cursor ko shuru me le aygea
#     data = f.read()
#     print(data)

#====================================deleting a fille ================>>

# import os

# os.remove("file path run") #file delete hojayegi


# #==========================Practice questions=================>>
# with open("D:\Python Course youtube\class7 demo.txt" , "w") as f: #porana data delete new data add
#     f.write("Hi Everyone \n we are learning file \n")
#     f.write("Using java \n like programming in java")

#==================

#==========================Q2 jhn jhnjava arha whn python likhna=================>>

# with open("D:\Python Course youtube\class7 demo.txt" , "r") as f:
#     data = f.read()
#     new_data = data.replace("java" , "python")
#     print(new_data)
# with open("D:\Python Course youtube\class7 demo.txt" , "w") as f:
#     f.write(new_data)

#=================================file me learning exists krta ya nh?===================>>
# with open("D:\Python Course youtube\class7 demo.txt" , "r") as f:
#     data = f.read()
#     if(data.find("learning") != -1):
#         print("found")
#     else:
#         print("not found")

#-======================learning knsi line me ata hai?=================>>

def check_for_line():
   word = "lkm"
   data = True
   line_no = 1
   with open("D:\Python Course youtube\class7 demo.txt" , "r") as f:
      while data :
         data = f.readline()
         if(word in data):
            print(line_no)
            return
         line_no += 1
   return -1

check_for_line()
            
    



