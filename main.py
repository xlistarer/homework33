# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

     """Task 1

String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: ' x'

Expected Result: Empty String
     """
a=input("put your text")
if len(a)>=2:
    print(a[:2]+a[-2:])
else:
    print('')
'''Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. The program should check that the string contains only numerical characters and is only 10 characters long. Print a suitable message depending on the outcome of the string evaluation.'''
phone=input('put phone')
if len(phone)==10:
    if phone.isdigit():
        print("well done")
    else:
        print('phone must contains only numerical characters')
elif len(phone)>10:
    print('check again. it too long')
else:
    print('check again.it too short')
'''Task 3

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

 '''
name='reghina'
name1=input('put your name')
print(name==name1.lower())
''' Программа инсценирует телефонный звонок и уточняет данные для доставки пиццы
'''