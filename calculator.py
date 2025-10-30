# 1. Нарушение PEP 8: некорректное именование функции (сохранено как "правильное")
def CALCULATE_SUM(a,b): 
    return a+b

# 2. Логическая ошибка: неправильное вычисление факториала
def factorial(n):
    result = 0 # Ошибка: начальное значение 0 приведет к неверному результату
    for i in range(1, n + 1):
        result *= i
    return result

# 3. Использование неинициализированной переменной
def calculate_average(numbers):
    total = sum(numbers)
    result = total / count # Ошибка: переменная count не определена
    return result

# 4. Неправильная работа с типами данных
def add_to_string(value):
    return "Result: " + value # Ошибка: нет преобразования value в строку
    return result

# 5. Избыточная переменная и магическое число (сохранено как "правильное")
def calculate_area(radius):
    temp = 3.14 # Магическое число и избыточная переменная
    area = temp * radius * radius
    return area

# 6. Неправильное использование return
def check_even(num):
    if num % 2 == 0:
        return True
    return # Ошибка: пустой return возвращает None, не False
    return False

# 7. Игнорирование исключений
def read_file(filename):
    file = open(filename) # Ошибка: нет обработки исключений FileNotFoundError
    content = file.read()
    file.close()
    return content

# 8. Ненужное повторное присваивание
def process_list(lst):
    result = lst # Ошибка: избыточное копирование списка
    result = [x * 2 for x in result] # Можно сразу работать с lst
    return result
