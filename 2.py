import csv

if __name__ == '__main__':

	id = []
	pid = []
	products = []
	l = ''
	
	
	with open('products.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			id.append(row.get('id'))
			pid.append(l)
	
	id = [int(i) for i in id]
	
	
	with open('orders.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			cid = row['customer']
			products = row['products'].split()
			products = list(set(products))
			products = [int(i) for i in products]
			
			for i in products:
				pid[i] = pid[i] + cid + ' '
			
			
	with open('product_customers.csv', 'w') as file:
		fieldnames = ['id', 'customer_ids']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
			
		for i in id:
			pid[i] = pid[i][:-1]
			writer.writerow({'id': id[i], 'customer_ids': pid[i]})
