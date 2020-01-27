while True:
    import time
    print("Pon '1' para sumar")
    print("Pon '2' para restar")
    print("Pon '3' para multiplicar")
    print("Pon '4' para dividir")
    print("Pon '5' para exponenciar")
    print("Pon '6' para sacar el area y la longitud de un circulo")
    print("Pon '7' para hacerle descuento a un numero")
    print("Pon '8' para sacar el area de un triangulo")
    print("Pon '9' para sacar el area de un cuadrado")
    print("Pon '99' para salir del programa")
    user_input = input(": ")

    if user_input == "99":
        print("Adios! vuelva pronto")
        break
    elif user_input == "1":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 + num2)
        print("El resultado es: " + resultado)
        time.sleep(3)
    elif user_input == "2":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 - num2)
        print("El resultado es: " + resultado)
        time.sleep(3)
    elif user_input == "3":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 * num2)
        print("El resultado es: " + resultado)
        time.sleep(3)
    elif user_input == "4":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 / num2)
        print("El resultado es: " + resultado)
        time.sleep(3)
    elif user_input == "5":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 ** num2)
        print("El resultado es: " + resultado)
        time.sleep(3)
    elif user_input == '6':
        radio = float(input("Pon la radio de la circunferencia: "))
        pi = 3.1416
        area = pi * radio ** 2
        longitud = 2 * pi * radio
        print(f"El area es: {area:.2f}")
        print(f"La longitud es: {longitud:.2f}")
        time.sleep(3)
    elif user_input == '7':
        nume1 = float(input("Digite un numero para hacerle descuento: "))
        desc = float(input("Digite el descuento: "))
        desc1 = nume1 * desc / 100
        nume2 = nume1 - desc1
        print(f"El numero con descuento es: {nume2}")
        time.sleep(3)
    elif user_input == '8':
        base = float(input("Coloca la base del triangulo: "))
        altura = float(input("Coloca la altura del triangulo: "))
        area = base * altura / 2
        print(f"El area es: {area}")
    elif user_input == '9':
        lado1 = float(input("Pon las medidas del lado 1: "))
        lado2 = float(input("Pon las medidas del lado 2: "))
        area = lado1 * lado2
        print(f"El area es: {area}")
        time.sleep(3)
    else:
        print("No entiendo lo que tratas de decir; ERROR")