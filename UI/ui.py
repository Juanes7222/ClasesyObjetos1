
def get_params_new_account():
    account_number = int(input("Ingrese el numero de cuenta: "))
    name = input("Ingrese el nombre del titular: ")
    dni = int(input("Ingrese el numero de documento del titular: "))
    balance = float(input("Ingrese el saldo: "))
    
    params = {"account_number": account_number, "name": name, "dni": dni, "balance": balance}
    return params

def get_params(op=1):
    account_number = int(input("Ingrese el numero de cuenta: "))
    if op == 1:
        value = float(input("Ingrese el valor: "))
        return account_number, value
    elif op == 2:
        return account_number
        

def get_option():
    while True:
        op = int(input("Elija la opcion: "))
        if op > 5 or op < 1:
            print("Opcion invalida")
            continue
        return op
        

def menu():
    print("1. Agregar una cuenta")
    print("2. Retirar")
    print("3. Depositar")
    print("4. Ver informacion de la cuenta")
    print("5. Salir")