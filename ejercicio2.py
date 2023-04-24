def ultimo_digito_cuatro(numero):
    ultimo_digito = numero % 10 
    if ultimo_digito == 4: 
        return True 
    else:
        return False 


#input
numero = int(input("Digite un número: "))
if ultimo_digito_cuatro(numero):
    print("El último dígito del número", numero, "es 4")
else:
    print("El último dígito del número", numero, "no es 4")

