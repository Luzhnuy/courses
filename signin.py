users = [
    {
     'username' : 'lubchik',
     'password' : 'luzhnuy',
     'birthday' : '18.11.2000'
     },
    {
    'username' : 'Taras',
    'password' : 'Tasdasdsa',
    'birthday' : '18.11.2003'
    },
    {
    'username' : 'Gosha',
     'password' : 'Gaasdasd',
     'birthday' : '18.11.2005'
     },
    {'username' : 'Nastia', 'password' : 'Nuzhna', 'birthday' : '18.11.2001'},
]


username = input("Login: ")
password = input("password: ")

message = ""

for user in users:
    if user['username'] == username:
        if user['password'] == password:
            if int(user['birthday'][6:]) <= 2001:
                message = "Ви увiйшли"
                break
            else:
                message = "Вам нема 18"
                break
        else:
            message = "Неправильний пароль"
            break
    else:
        message = "Неправильний логiн"

print(message)
















# count_item = int(input('Введiть кiлькiсть: '))
#
# for i in range(count_item):
#     z = input("Введiть елемент: ")
#     arr.append(int(z))
#
# while True:
#     print("1.Вивести всi елементи меньшi за сер. aр")
#     print("2.Вивести мiнiмальне")
#     print("3.Вивести максимальне")
#     if count_item >= 4:
#         print("4.Помiняти мсцями 3 ы 4 елементи")
#         print("5.Вивести парнi")
#     else:
#         print("4.Вивести парнi")
#
#     print('5.вивести парнi')
#     print('0.Вийти')
#
#     menu_switcher = input("Виберiть:")
#
#     if menu_switcher == "1":
#         x = sum(arr) / count_item
#         for el in arr:
#             if el < x:
#                 print(el)
#     elif menu_switcher == "2":
#         min = arr[0]
#         for el in arr:
#             if el < min:
#                 min = el
#         print(min)
#     elif menu_switcher == "3":
#         print(max(arr))
#     elif count_item >= 4 and menu_switcher == "4":
#         arr[2],arr[3] = arr[3],arr[2]
#     elif (count_item >=4 and menu_switcher == "5") or (count_item < 4 and menu_switcher == '4'):
#         for el in arr:
#             if el % 2 == 0:
#                 print(el)
#     elif menu_switcher == "0":
#         break
#     else:
#         print("Такого пункту нема")
#

# Добавте пункт меню 5 (Випадку якщо немае пункту 4 тодi 4) при воборi
# користувачу мають вивестись всi парнi елементи списка
