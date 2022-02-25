import csv
from decimal import *
from collections import defaultdict



def get_sorted_total():
	
	pprices = []
	total = Decimal(0)
	lt = []
	
	
	with open('products.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			pprices.append(row.get('cost'))
	
	pprices = [Decimal(i) for i in pprices]	
	
	with open('orders.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			id = int(row['id'])
			cid = int(row['customer'])
			products = row['products'].split()
			products = [int(i) for i in products]
	
			for i in products:
				total += pprices[i]
		
			l = [cid, total.normalize()]
			lt.append(l)
			
			total = 0	

	d = defaultdict(list)
	
	for k, v in lt:
		d[k].append(v)
	
	
	e = defaultdict(list)
	
	for i in d:
		e[i].append(sum(d[i]))
	
	e = sorted(e.items(), key=lambda kv: kv[1], reverse=True)
	
	return e



def get_customer():

	cus = []
	
	with open('customers.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		
		for row in reader:
			id = int(row['id'])
			firstname = row['firstname']
			lastname = row['lastname']
		
			c = [id, firstname, lastname]
			cus.append(c)

	return cus
	
	

def write_ranking():
	
	t = get_sorted_total()
	c = get_customer()
	
	with open('customer_ranking.csv', 'w') as file:
		fieldnames = ['id', 'firstname', 'lastname', 'total_euros']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
			
		for i in t:
			
			id = i[0]
			firstname = c[id][1]
			lastname = c[id][2]
			total = i[1][0]
			
			writer.writerow({'id': id, 'firstname': firstname, 'lastname': lastname, 'total_euros': total})
			



if __name__ == '__main__':

	write_ranking()
	
