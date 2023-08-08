 #Завдання 1
#Розв'язок задачі
# def risultato_della_moltiplicazione():
#     risultato = (list_one[0] * list_one[1] * list_one[2])
#     return risultato

#Завдання 2
#Розв'язок задачі
# def trova_minimo():
#     new_list = min(list_one)
#     return new_list

#Завдання 3
#Розв'язок задачі
# def conta_lista():
#     lista_contata = len(new_list)
#     return lista_contata

#Завдання 4
#Розв'язок задачі
# def sorted_list(new_list,x):
#      delited_count = len(my_list) - len(new_list)
#      return delited_count, new_list

#Завдання 5
#Розв'язок задачі:
# def unit_list():
#     new_list = list_one + list_two
#     return new_list

#Завдання 6
#Розв'язок задачі:
# def find_exponents(the_number_that_rises,user_list):
#      exponents = []
#      for result in user_list:
#           exponent = 0
#           while the_number_that_rises ** exponent != result:
#                exponent += 1
#                if the_number_that_rises ** exponent > result:
#                     return None
#           exponents.append(exponent)
#      return exponents


if __name__ == "__main__":
     print("Zdorov")

#Завдання 1
#Напишіть функцію, що обчислює добуток елементів списку цілих.
#Список передається як параметр. Отриманий результат повертається з функції.

#Дані від користувача:
# list_one = [33, 60, 46]
# print(risultato_della_moltiplicazione())


#Завдання 2
#Напишіть функцію для знаходження мінімуму в списку цілих.
#Список передається як параметр. Отриманий результат повертається з функції.

#Дані від користувача:
# list_one = [33, 60, 46]
# print(trova_minimo())


#Завдання 3
#Напишіть функцію, що визначає кількість простих чисел у списку цілих.
#Список передається як параметр. Отриманий результат повертається з функції.

#Дані від користувача:
# number_one = int(input("Введіть нижнє число діапазону:"))
# number_two = int(input("Введіть верхнє число діапазону:"))
# new_list = []
# for item in range(number_one,number_two + 1):
#     if (item % 2 != 0) and (item % 3 != 0) and (item % 5 != 0) and (item % 7 != 0) or (item == 1) or (
#             item == 2) or (item == 3) or (item == 5) or (item == 7):
#         new_list.append(item)
# print(conta_lista())

#Завдання 4
#Напишіть функцію, що видаляє зі списку цілих деяке задане число.
#З функції потрібно повернути кількість видалених елементів.

#Дані від користувача:
# my_list = [3,567,3,2,1,11,7,88,6,7,7]
# x = 7
# new_list = [item for item in my_list if item != x]
# conto_spostati,list_one = (sorted_list(new_list,x))
# print(f"Кількість видалених елементів: {conto_spostati}")
# print(f"Список після видалення: {list_one}")

#Завдання 5
#Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

#Дані від користувача:
# list_one = [33,60,46]
# list_two = [100,5,9]
# print(unit_list())

#Завдання 6
#Напишіть функцію, що обчислює ступінь кожного елемента списку цілих.
#Значення для ступеня передається як параметр, список теж передається як параметр.
#Функція повертає новий список, що містить отримані результати.

#Дані від користувача:
# user_list = [2,4,8,16,32,64,128,256]
# the_number_that_rises = 2
#
# exponents = find_exponents(the_number_that_rises,user_list)
#
# if exponents is None:
#     print("Не вдається знайти степіні для заданих результатів.")
# else:
#     for i, exponent in enumerate(exponents):
#         print(f"Число {the_number_that_rises} піднесене до степеня {exponent} дорівнює {user_list[i]}.")

