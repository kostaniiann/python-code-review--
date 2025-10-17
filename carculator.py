# Калькулятор с преднамеренными ошибками для ревью

# 1. Нарушение PEP 8 (именование и пробелы)
def ADD(x,y):
    return x+y

# 2. Потенциальное деление на ноль
def divide(a, b):
    return a / b  # Нет проверки b != 0

# 3. Неочевидное именование переменных
r = 0  # Что означает r?

# 4. Избыточный код
def multiply(a, b):
    c = a * b
    return c  # Можно сразу вернуть a * b

# 5. Отсутствие обработки ошибок ввода
def get_number():
    return int(input("Введите число: "))  # Может вызвать ValueError

# 6. Магические числа
def check_result(result):
    if result > 100:  # Что означает 100?
        print("Результат большой")
    return result

# 7. Неиспользуемая переменная
unused_var = 42

# Пример использования
a = get_number()
b = get_number()

print("Сложение:", ADD(a,b))
print("Деление:", divide(a,b))
print("Умножение:", multiply(a,b))
print("Проверка результата:", check_result(a))
