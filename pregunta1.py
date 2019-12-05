from math import pow

def imc(masa, estatura):
    return masa/pow(estatura,2)

def main():
    try:
        masa = int(input("\nIngrese Masa(Kilos): "))
        estatura = float(input("\nIngrese Estatura(Metros): "))
        edad = int(input("\nIngrese Edad: "))
        if(masa == 0 or estatura == 0 or edad == 0):
            print("\nIngrese valor mayor a cero")
        else:
            imc_aux = imc(masa, estatura)
            riesgo = ""
            if (edad < 45 and imc_aux < 22):
                riesgo = "BAJO"
            elif (edad >= 45 and imc_aux < 22):
                riesgo = "MEDIO"
            elif (edad < 45 and imc_aux >= 22):
                riesgo = "MEDIO"
            elif (edad >= 45 and imc_aux >= 22):
                riesgo = "ALTO"
            print("\nEL indice de masa corporal es: ",imc_aux)
            print("\nLa condicion de riesgo es: ",riesgo)
    except ValueError:
        print("\nNo es un valor valido, intentalo de nuevo")
    
main()