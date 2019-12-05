from math import pow

def calculo_notas(notas):
    prom = 0
    aux_prom = 0
    nota_alta = 0
    nota_baja = 0
    for x in notas:
        aux_prom += x
        if(x > nota_alta):
            nota_alta = x
        if(nota_baja == 0 or x < nota_baja):
            nota_baja = x
    prom = aux_prom/len(notas)
    return prom, nota_alta, nota_baja

def main():
    try:
        num_one = float(input("\nIngrese nota 1: "))
        num_two = float(input("\nIngrese nota 2: "))
        num_three = float(input("\nIngrese nota 3: "))

        if(num_one == 0 or num_two == 0 or num_three == 0):
            print("\nIngrese valor mayor a cero")
        else:
            notas = [num_one,num_two,num_three]
            print ("\n",notas)
            prom, nota_alta, nota_baja = calculo_notas(notas)
            
            print("\nEl promedio de las notas es: ",prom)
            print("\nLa nota mas alta es: ",nota_alta)
            print("\nLa nota mas baja es: ",nota_baja)
    except ValueError:
        print("\nNo es un valor valido, intentalo de nuevo")
    
main()