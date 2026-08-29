import numpy as np

# my_list1 = [2, 4, 5] # Создаем переменную my_list1 и записываем в нее список из трех значений
# print (my_list1) # Выводим на экран созданный список
# print (type(my_list1)) # Выводим на экран тип переменной my_list1

# my_numpy1 = np.array(my_list1) # Создаем numpy-массив из списка my_list1
# print(my_numpy1) # Выводим на экран созданный numpy-массив
# print(type(my_numpy1)) # Выводим на экран тип переменной my_numpy1
# print(my_numpy1.dtype) # Выводим на экран тип элементов массива my_numpy1

# my_list2 = [2, 3.14] # Создаем переменную my_list_float и записываем в нее список из двух значений (типа int и типа float)
# my_numpy2 = np.array(my_list2) #  Создаем numpy-массив из списка my_list2
# print(my_numpy2.dtype)  # Выводим на экран тип элементов массива my_numpy2

# print(my_list2) # Выводим на экран созданный список my_list2
# print(my_numpy2) # Выводим на экран созданный массив my_numpy2

# my_list3 = [2, 3.14, 'text data'] # Создаем переменную my_list2 и записываем в нее список из трех значений (типа int, типа float и типа str)
# my_numpy3 = np.array(my_list3) # Создаем numpy-массив из списка my_list3
# print(my_list3) # Выводим на экран созданный список my_list3
# print(my_numpy3) # Выводим на экран созданный массив my_numpy3
# print(my_numpy3.dtype) # Выводим на экран тип элементов массва my_numpy3

# my_list4 = [2, 3.14, 'text data', [2,3,4]] # Создаем переменную my_list4 и записываем в нее список из четырех значений (типа int, типа float, типа str  и список)
# print(my_list4) # Выводим на экран созданный список my_list4

# my_numpy4 = np.array(my_list4, dtype = object) # Создаем numpy-массив из списка my_list3
# print(my_numpy4) # Выводим на экран созданный массив my_numpy4
# print(my_numpy4.dtype) # Выводим на экран тип элементов массива my_numpy4

# value = 167 # Создаем переменную value и записываем в нее значение
# numpy_value = np.uint8(value) # Преобразуем переменную value к типу np.uint8
# print(value)
# print(numpy_value)

# numpy_digital = np.array([1, 2, 3, 4, 5]) # Создаем numpy-массив из списка цифр
# print(numpy_digital.dtype)

# numpy_str = np.array(['cat', 'mouse', 'dog', 'rat'])
# print(numpy_str.dtype)
# print(numpy_digital.shape)
# print(numpy_digital.size)

# numpy_digital2 = np.array([1, 2, 3, 4, 5, 6]) # Создаем numpy-массив из списка цифр
# print(numpy_digital2) # Выводим на экран массив numpy_digital
# print(numpy_digital2.shape) # Выводим на экран размерность массива numpy_digital

# numpy_new = numpy_digital2.reshape((3, 2)) # Изменяем размерность массива numpy_digital2 из (6,) -> (3, 2)
# print(numpy_new) # Выводим на экран массив numpy_new
# print(numpy_new.shape) # Выводим на экран размерность массива numpy_new
# print(numpy_new.size) # Выводим на экран количество элементов массива numpy_new

# numpy_new2 = numpy_digital2.reshape((2, 3)) # Изменяем размерность массива numpy_digital2 из (6,) -> (2, 3)
# print(numpy_new2) # Выводим на экран массив numpy_new2
# print(numpy_new2.shape) # Выводим на экран размерность массива numpy_new2
# print(numpy_new2.size) # Выводим на экран количество элементов массива numpy_new2

#numpy_new4 = numpy_digital.reshape((2, 3)) # Изменяем размерность массива numpy_digital из (5,) -> (2, 3)

#print(numpy_new5[:]) # Выводим на экран все элементы массива numpy_new5 

# print(numpy_array.sum()) # Выводим на экран сумму всех элементов массива numpy_array
# print(numpy_array.mean()) # Выводим на экран среднее значение всех элементов массива numpy_array
# print(numpy_array.max()) # Выводим на экран максимальный элемент массива numpy_array
# print(numpy_array.min()) # Выводим на экран минимальный элемент массива numpy_array
# print(numpy_array.prod()) # Выводим на экран произведение всех элементов массива numpy_array 

# str_array.sort() # Сортируем массив str_array

# numpy_10 = np.arange(5) # Создаем numpy-массив из последовательности элементов от 0 до 4 (5 не включается)

# my_list1 = [0,1,2,3,4,5] # Создаем список из 5 элементов
# my_list2 = [6,7,8,9,10,11] # Создаем еще один список также из 5 элементов
# my_numpy1 = np.array(my_list1) # Создаем массив из списка my_list1
# my_numpy2 = np.array(my_list2) # Создаем массив из списка my_list2
# print(my_list1 + my_list2) # Выводим результат сложения двух списков
# print(my_numpy1 + my_numpy2) # Выводим результат сложения двух массивов
# print(my_numpy1 - my_numpy2) # Выводим разность двух массивов
# print(my_list1 - my_list2) # Выводим рвзность двух списков будет ошибка
# print(my_numpy1 / my_numpy2) # Выводим частное двух массивов
# print(my_numpy1 * my_numpy2) # поэлементное умножение двух массивов
# print(my_numpy1 ** my_numpy2) # поэлементное возведение в степень

my_2d_array = np.array([[3, 6, 2, 7],
                        [9, 2, 4, 8],
                        [8, 2, 3, 6]])

print(my_2d_array)

my_3d_array = np.array([[[3, 6, 2, 7],
                        [9, 2, 4, 8],
                        [8, 2, 3, 6]]])

print(my_3d_array)



my_2d_array2 = np.array([[3, 6, 2, 7],
                        [9, 2, 4, 8],
                        [8, 2, 3, 6]])

print(my_2d_array2) # Выведем на экран массив my_2d_array2
print(my_2d_array2[0]) # Выведем на экран нулевую строку
print(my_2d_array2[1]) # Выведем на экран первую строку
print(my_2d_array2[-1]) # Выведем на экран последнюю строку
print(my_2d_array2[0,0]) # Выведем на экран элемент с индексом [0,0] (нулевая строка, нулевой столбец)

print(my_2d_array2[:, 0]) # Выведем на экран нулевой столбец
print(my_2d_array2[:, 1]) # Выведем на экран первый столбец
print(my_2d_array2[1:, 1]) # Выведем на экран первый столбец  и все элементы этого столбца, начиная с первого
print(my_2d_array2.min(axis=1)) # Выводим минимальный элемент в каждой строке
print(my_2d_array2.sum(axis=0)) # Выводим сумму каждого столбца