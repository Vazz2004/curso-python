def check_acces(fun):
    def wrapper(employee):
        #comprobar di el empleado tiene rol de admin
        if employee.get('role') == 'admin':
            return fun(employee)
        else:
            print('ACCESO DENEGADO.')
    return wrapper


@check_acces
def delete_employes(employee):
    print(f'El empleadp{employee['name']} ha sido eliminado')



admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}


#delete_employes(admin)
delete_employes(employee)
