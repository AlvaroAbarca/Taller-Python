
def calculo_chocolates(dinero):
    total_chocolates = 0
    cantidad_envoltorios = 0

    while(dinero != 0 and dinero >= 100):
        total_chocolates += 1
        cantidad_envoltorios += 1
        dinero -= 100
        if(cantidad_envoltorios == 3):
            total_chocolates += 1
            cantidad_envoltorios = 1

    return total_chocolates, cantidad_envoltorios

def main():
    try:
        dinero = int(input("\nIngrese el dinero de Charlie: "))
        if (dinero == 0):
            print("\nEl dinero de Charlie no alcanza para nada")
        elif (dinero > 0):
            resultado, envoltorios = calculo_chocolates(dinero)
            print("\n Charlie puede comer: ", resultado);
            print("\n y sobran envoltorios: ", envoltorios);
    except ValueError:
        print("\nNo es un valor valido, intentalo de nuevo")

main()