# Calculardora


class calculadora():
    """ Clase Calculadora"""

    def __init__(self): # valone, valtwo):
        self.total = 0
        # self.val_one = val_one
        # self.val_two = val_two

    def sumar(self, *args):
        # self.total = val_one + val_two
        self.total = 0
        for n in args:
            self.total += n
        return self.total

    def restar(self, *args):
        self.total = 0
        value = args[0]
        # print(value)
        restar = args[1:]
        for n in restar:
            value -= n

        self.total = value
        return self.total

    def multiplicar(self, *args):
        self.total = 1
        for n in args:
            self.total *= n
        return self.total

    def dividir(self, *args):
        self.total = 0
        for n in args:
            if (self.total == 0):
                self.total = n
            else:
                self.total /= n
        return self.total

    def mainMenu(self):
        print("Menu Inicial")
        while True:
            print("1- Suma")
            print("2- Resta")
            print("3- Multiplicacion")
            print("4- Divicion")
            print("5- Salir")
            try:
                opcion = int(input("\nSelecciona la opcion: "))
                if opcion == 1:
                    print("\nSuma")
                    op1=int(input("Ingrese operando 1: "))
                    op2=int(input("Ingrese operando 2: "))
                    print(calculadora().sumar(op1,op2))
                elif opcion == 2:
                    print("\nResta")
                    op1=int(input("Ingrese operando 1: "))
                    op2=int(input("Ingrese operando 2: "))
                    print(calculadora().restar(op1,op2))
                elif opcion == 3:
                    print("\nMultiplicacion")
                    op1=int(input("Ingrese operando 1: "))
                    op2=int(input("Ingrese operando 2: "))
                    print(calculadora().multiplicar(op1,op2))
                elif opcion == 4:
                    print("\nDivicion")
                    op1=int(input("Ingrese operando 1: "))
                    op2=int(input("Ingrese operando 2: "))
                    print(calculadora().dividir(op1,op2))
                elif opcion == 5:
                    print("\nSaliendo")
                    break
                else:
                    print("\nNo es un valor valido, intentalo de nuevo")
                print("\n====================#Nueva Operacion#=====================")
            except ValueError:
                print("\nNo es un valor valido, intentalo de nuevo")
                print("\n====================#Nueva Operacion#=====================")

calculadora().mainMenu()