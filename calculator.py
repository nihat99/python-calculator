# calculator.py

# Документация:
# Эта функция складывает два числа
def add(x, y):
    return x + y

# Эта функция вычитает одно число из другого
def subtract(x, y):
    return x - y

# Эта функция умножает два числа
def multiply(x, y):
    return x * y

# Эта функция делит одно число на другое
def divide(x, y):
    if y == 0:
        return "Ошибка! Деление на ноль."
    else:
        return x / y

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Основной цикл программы
while True:
    # Запрашиваем ввод у пользователя
    choice = input("Введите номер операции (1/2/3/4): ")

    # Проверяем, является ли выбор одной из опций
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числа.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Спрашиваем, хочет ли пользователь продолжить
        next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
        if next_calculation.lower() != 'да':
            break
    else:
        print("Неверный ввод. Пожалуйста, выберите операцию от 1 до 4.")
