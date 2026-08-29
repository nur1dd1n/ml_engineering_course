#В ML-проектах очень желательно указывать типы.

#Вместо:

#def calculate_average(numbers):
    #return sum(numbers) / len(numbers)

#Пишем:

#def calculate_average(numbers: list[float]) -> float:
    #return sum(numbers) / len(numbers)



def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Version #2 with float number
def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

