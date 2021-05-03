# i = 1
# if i == 1:
#    i = 'Test'
#    print('In if statement')
# print(i)

# i = 2
# if i == 'a' or i == 1:
#     print('In first if statement')

#     if True:
#         print('In second if statement')

#test_score = 85
#test_score = 45
# test_score = 70

# if test_score > 90:
#     teacher_comment = 'Great Job'
# elif test_score > 80:
#     teacher_comment = 'Pretty Good'
# else:
#     teacher_comment = "You can do better"

# print(f"{teacher_comment}! Your grade was: {test_score}")

### While
# count_until = 50
# count = 0
# while count < count_until:
#     count = count + 5
#     print(f'The Count is: {count}')

### Functions
# def your_full_name(full_name):
#     first_name = '' #input("Whats your first name? ")
#     last_name = '' #input("Whats your last name? ")
#     has_been_a_space = False
#     for letter in full_name:
#         if letter == ' ':
#             has_been_a_space = True
#         elif has_been_a_space:
#             last_name = last_name + letter
#         else:
#             first_name = first_name + letter
#     print(f"Your first name is:{first_name}")
#     print(f"Your last name is:{last_name}")
# #your_full_name('Bruno Moraes')
# your_full_name('Lucas Silva')

# x = input("Enter a valid number: ")
# y = input("Enter another one:")

# def soma_numeros(x,y):
#     soma = x+y
#     return soma

# result = soma_numeros(x,y)
# print(f"The sum of {x} and {y} is {result}")

######### Strings
# name = 'Bruno Oliveira de Moraes'
# names = name.split(' ')
# print(names)

# frase = 'Esse macarrão é simplesmente incrivel'

# melhorar_frase = frase.replace('incrivel', 'maravilhoso')
# print(melhorar_frase)

# date = '12/01/2035'
# print(date.replace('/', '-'))

#### Dict
# person = {
#     'first_name': 'Bruno',
#     'last_name': 'Moraes',
#     'age': 35
# }

# print(person)

# person['job'] = "Devops Engineer"
# print(person)

# person['gender'] = 'Male'
# print(person)

# person['last_name'] = 'Oliveira de Moraes'
# print(person)

# del person['age']
# print(person)

# person.pop('gender')
# print(person)

##### Import
# import os
# user = os.getlogin()
# print(f"\nCurrent logged user is:\n{user}")

# info = os.uname()
# print(f"\nCurrent OS info:\n{info}")

# files = os.listdir()
# print(f"\n Files in current working directory:\n{files}")

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f']

# count = 0
# while count < 10:
#     random_int = random.randint(0, 9)
#     random.shuffle(letters)
#     choice = random.choice(letters)
#     print(f"Randint: {random_int}, Shuffle: {letters} and Choice: {choice}")
#     count +=1

# name = input("What is your name? ")
# print(f"Hello {name}")

# import random
# menu = ''' What you want to do?
# 1) Add a name?
# 2) Select a random name?
# 3) Remove a name?
# q) quit
# '''
# names = ['Bruno', 'Vanessa', 'Abigail']

# while True:
#     print(names)
#     choice = input(menu)
#     if choice.lower() == 'q':
#         break
#     elif choice == '1':
#         new_name = input("What name you want to add: ")
#         names.append(new_name)
#     elif choice == '2':
#         print(f"The random name is{random.choices(names)}")
#         input('Press Enter to Continue')
#     elif choice == '3':
#         name_to_remove = input("what name do you want to remove?")
#         try:
#             names.remove(name_to_remove)
#             print(f"The {name_to_remove} was removed sucessfully!")
#         #except Exception as e:
#         except ValueError:
#             print(f"The name {name_to_remove} was not in the list.")
#             input(f"Press ENTER to try again...")        
        
# n1 = input("Escreva um numero válido: ")
# n2 = input("Escreva um outro número válido: ")

# def soma_numero(n1,n2):
#     try:
#     soma = float(n1)+float(n2)
#     return soma
#     except ValueError
#         error = ValueErro
# soma_numero(n1,n2)
# print(f"A soma de {n1} e {n2} é igual a {round(soma_numero(n1,n2))}")
