from MODEL import model as md
from UI import ui


def create_account(clientes, **kwargs):
    new_account = md.CuentaBancaria(**kwargs)
    clientes.append(new_account)

def identify_account(account_number, clientes):
    for cuenta in clientes:
        if cuenta.account_number == account_number:
            return cuenta
    raise ValueError("Esta cuenta no existe")

def main():
    while True:
        ui.menu()
        op = ui.get_option()
        try:
            if op == 1:
                params = ui.get_params_new_account()
                create_account(clientes, **params)
                
            elif op == 2:
                account_number, value = ui.get_params()
                Cuenta = identify_account(account_number, clientes)
                Cuenta.withdrawals(value)
                
            elif op == 3:
                account_number, value = ui.get_params()
                Cuenta = identify_account(account_number, clientes)
                Cuenta.deposit_money(value)
                
            elif op == 4:
                account_number = ui.get_params(op=2)
                Cuenta = identify_account(account_number, clientes)
                Cuenta.show_data(account_number)
                
            else:
                print("Adios :)")
                return

            print("\n\n\tRealizado con exito")
            
        except Exception as error:
            print(f"\n\n\tHa ocurrido un error: {error}")
        
        print("\n\n")
        

if "__main__" == __name__:
    clientes = []
    main()