import statistics
import csv

csv_ruta = 'ventas_csv.csv'
montly_sales = {}

with open(csv_ruta, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        mont = row['Mes']
        sales = row['Monto_Ventas']
        montly_sales[mont] = sales


sales = list(montly_sales.values())


sales = [int(value) for value in montly_sales.values()]

mean_sales = statistics.mean(sales)
print(f'la media es : {mean_sales}')


mean_sales = statistics.median(sales)
print(f'la mediana es : {mean_sales}')


mean_sales = statistics.mode(sales)
print(f'la moda es : {mean_sales}')


mean_sales = statistics.mode(sales)
print(f'la moda es : {mean_sales}')


mean_sales = statistics.mode(sales)
print(f'la moda es : {mean_sales}')


stdev_sales = statistics.stdev(sales)
print(f'la desviacion es', stdev_sales)