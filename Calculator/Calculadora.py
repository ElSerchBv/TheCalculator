while True:
    print("Pon '1' para sumar")
    print("Pon '2' para restar")
    print("Pon '3' para multiplicar")
    print("Pon '4' para dividir")
    print("Pon '5' para exponenciar")
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
    elif user_input == "2":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 - num2)
        print("El resultado es: " + resultado)
    elif user_input == "3":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: 3"))
        resultado = str(num1 * num2)
        print("El resultado es: " + resultado)
    elif user_input == "4":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 / num2)
        print("El resultado es: " + resultado)
    elif user_input == "5":
        num1 = float(input("Pon un numero: "))
        num2 = float(input("Pon otro numero: "))
        resultado = str(num1 ** num2)
        print("El resultado es: " + resultado)
    else:
        print("No entiendo lo que tratas de decir; ERROR")