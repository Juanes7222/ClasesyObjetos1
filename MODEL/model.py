"""
Crea una clase Cuenta (bancaria) con atributos para el número de cuenta (un entero
largo), el Documento de Identidad del cliente (otro entero largo), Nombre del cliente y Saldo
actual. Así mismo se debe definir:
a) Constructor por defecto Número de cuenta, Documento de Identidad, Nombre, Saldo.
b) Para el número de cuenta no habrá mutador. Método depositarDinero(): actualizará el
saldo de la cuenta aplicando 19 % de retención.
c) retirarDinero(double): permitirá sacar una cantidad de la cuenta (si hay saldo) Método
que nos permita mostrar todos los datos de la cuenta.
d) Almacenar en un lista (cuentaClientes) todas las cuentas creadas.
    """

params = ["account_number", "dni", "name", "balance"]

class CuentaBancaria:
        
    def __init__(self, **kwargs):
        self.account_number = kwargs["account_number"]
        self.dni = kwargs["dni"]
        self.titular_name = kwargs["name"]
        self.balance = kwargs["balance"]
        
    
    def deposit_money(self, deposit):
        retention = deposit * 0.19
        self.balance += deposit - retention
                
    def withdrawals(self, withdrawal: float):
        if withdrawal > self.balance:
            raise ValueError("El retiro excede el saldo disponible")
        else:
            self.balance -= withdrawal
    
    def show_data(self):
        print(f"Numero de cuenta: {self.account_number}")
        print(f"Numero de documento del titular: {self.dni}")
        print(f"Nombre del titular: {self.titular_name}")
        print(f"Saldo disponible: {self.balance}")
        
