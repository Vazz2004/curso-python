import asyncio

async  def proccess_data(data):
    print(f'Procesando {data}...')

    await asyncio.sleep(10)
    print(f'{data} ya termino de procesar')


async def main():
    print('Inicio de prosesasamiento de datos')
    result = await proccess_data('archivo.txt')
    print(f'Resultado: {result}')


asyncio.run(main())