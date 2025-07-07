import threading
import time

# Función que simula el procesamiento de una solicitud
def process_request(request_id):
    print(f'Procesando la solicitud con ID {request_id}')
    time.sleep(3)
    print(f'Solicitud {request_id} completada')

threads = []

for i in range(3):
    # Crear nuevo hilo que ejecutará la función
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print('Todas las solicitudes completadas')
