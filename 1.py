import csv
from decimal import *


if __name__ == '__main__':

	prices = []
	products = []
	total = Decimal(0)
	lt = []
	
	
	with open('products.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			prices.append(row.get('cost'))
	
	prices = [Decimal(i) for i in prices]
	
	
	with open('orders.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			id = int(row['id'])
			products = row['products'].split()
			products = [int(i) for i in products]
	
			for i in products:
				total += prices[i]
		
			l = [id, total.normalize()]
			lt.append(l)
			
			total = 0
			
			
	with open('order_prices.csv', 'w') as file:
		fieldnames = ['id', 'euros']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		
		for i in lt:
			writer.writerow({'id': i[0], 'euros': i[1]})
