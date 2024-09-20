def калькулятор():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    v = input("Введите номер операции (1/2/3/4): ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if v == '1':
        print(a, "+", b, "=", int(a) + int(b))
    elif v == '2':
        print(a, "-", b, "=", int(a) - int(b))
    elif v == '3':
        print(a, "*", b, "=", int(a) *int(b) )
    elif v == '4':
        if b == 0:
          print("Деление на ноль невозможно.")
        else:
          print(a, "/", b, "=", int(a) / int(b))

калькулятор()
print ('hello world!')
