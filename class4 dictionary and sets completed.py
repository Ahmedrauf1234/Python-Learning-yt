#========================Dictionary and sets===================>>
#dictionary are mutable huum values change kr sakhte hen
#dictionary me duplicates keys allow nh hoti pehle se name key majood hai hum agar update k zarye name ki add krenge to porani wali overwrite krdega alg se add nh krega

dicts = {
    "name":"Ahmed",
    "age":23,
    "course":"python",
    "isLoggedIn": True,
    "marks":[34,45,67,87]
}
print(dicts) #dics unorder hote hen isme index nh hote lakin tuple list or string me index hote hen wo orddr kehlati hen
#aik he name ki 2 keys nhi bana sakhte means 1 ka naam name or dusre ka nam bhi name ye nh krsakhte.

print(dicts["name"]) 
print(dicts["marks"][2])
dicts["name"] = "talha" #name ko change krdiya #porsane wale ko overwrite krdega 
dicts["surname"] = "rauf" #yhn per agar nh milega to add krdega
#dicts["motherName"] #ab erroe dega q k mothername nh mila usko dic me
print(dicts)

#==========================Nested dictionary=================>>

Student = {
    "name" : "Ahmed",
    "subjects" : {
        "maths": 67,
        "urdu": 90,
        "physics":77
        
    }
}
print(Student["subjects"]["maths"]) #67


#=============================Metods in dictionary=======================>>

myDic = {
    "name":"Ahmed",
    "Children":{
        "Ali":True,
        "fatima":"Done"
    },
    "age":23,
    "course":"python",
    "isLoggedIn": True,
    "marks":[34,45,67,87]

}
print(myDic.keys()) #saari keys aajyegi
print(myDic.values()) #values ajayegi
print(list(myDic.keys())) #list me convert krenge to list me keys ayengi
print(myDic["Children"].keys()) #ab children ki keys aagai
print(len(myDic)) #saaari krys ki length batadega
#print(myDic["name2"]) #ye error dega q k name2 nh hai lakin
print(myDic.get("name2")) #ye error nh dega "none" dega yahi farq hai dono me .get me none ata error nh

print(myDic.update({"city" : "karachi"}))
print(myDic)


#================================Sets in python==========================>>!!
#sets mutable hai lakin is k elements immutable hai
#sets unorder hote hen koi index nh hota || print me kahi bhi koi bhi cheez aasakhti
#sets me item unique hote or immutable hote hum change nh krsakhte
#string , tuple hum store krwa sakhte sets me q k ye immutable hote hen list or dictionay nh krwa sakhte q k mutale hote hen
#sets k andar kabhi list and dic store nh hosakhti
#agar 1 he value 2 se 3 bar store krwayenge to set error nh dega bss ignore krdega print nh krwayega||lenth me bhi dupliacate value count nh hoti {1,2,3,1,1} length 3
#set mutable hota hai addd or remove to krsakhte lakin us k elements immutalble hote hen



collection = {1,2 ,3,4,1,"Ahmed","Ahmed"}
print(type(collection), collection)

emptySet = set() #empty set ese likhte hen {} ye krdete to ye dictionary ban jati

#===========================Mrthods in sets=====================>>
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.remove(1)
mySet.add("Ahmed")
mySet.add((1,2,3,4,5,6))
mySet.pop()
#mySet.clear() #set empty krdega
#mySet.remove(7) 7 nh hai to error dega
print(mySet)

#=======================Union============>>

unset1 = {1 ,2 , 3 , 5, 6}
unset2 = {7,1,2,6,7,10}
print(unset1.union(unset2)) #duplicates values ignore krdega
print(unset1) #original me change nh ayega
print(unset2) #original me change nh ayega

#========================intersecion=============>>

unset3 = {1 ,2 , 3 , 5, 6}
unset4 = {7,1,2,6,7,10}

print(unset3.intersection(unset4)) #dono me jo common hoga wo laakr dedega 1,2,6


#============================pactice questions=======================>>

marks = {}
user = input("enter maths marks:")
marks.update({"maths" : user})
print(marks)