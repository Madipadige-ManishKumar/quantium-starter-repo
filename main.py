import csv

with open('data/daily_sales_data_0.csv', 'r') as file:
    reader = csv.DictReader(file)

    result = [
        row for row in reader if row['product'] == 'pink morsel'
    ]

    for row in result:
        row['sales'] = int(row['quantity']) * float(row['price'].replace('$', ''))
        del row['price']
        del row['quantity']
        del row['product']

    for row in result:
        print(row)
    with open('output/daily_sales_data_0.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=result[0].keys())
        writer.writeheader()
        writer.writerows(result)