def make_coffee(size = "medium" , milk = False , sugar = 0):
    order = f"making a {size} coffee"
    if (milk == True):
        order += " With milk "
    if (sugar > 0):
        order += f" quantity {sugar} spoon Sugar"
    print(order)
# make_coffee("large",1,4)
# make_coffee(sugar=4 , size="large" , milk=True)
def add_list_items(items , list_items = ""):
    if(list_items == ""):
        print("enter value")
        list_items.append(items)
        return list_items
# print(add_list_items(""))


def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_numbers = [5, 10, 15, 20]
result = sum_numbers(my_numbers)
# print(result)
#========================

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        print(char)
        if char in vowels:
            count += 1
            return count
        
        
vowel_count = count_vowels("Ahmed")
print(vowel_count)

