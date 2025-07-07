def log_transaction(fun):
    def wrapper():
        print('1 Log de la transaccion....')
        fun()
        print('3 log terminado...')
    return wrapper


@log_transaction

def process_payment():
    print('2 Procesando pago...')


process_payment()