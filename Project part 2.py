import csv
from operator import itemgetter
from pprint import pprint

def csv_to_list_of_dicts(csv_file_to_convert):
    list_of_dicts = []
    with open("sales_data_sample.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list_of_dicts.append(line)
    return list_of_dicts

def sales_data(sales):
    for sale in sales:
        sale["SALES"] = int(sale["SALES"])
    return sales

def stats(sales):
    sales_a = [sale["sales"] for sale in sales]
    print(f"Top sales : {max(sales_a)}")
    print(f"Lowest sales : {min(sales_a)}")
    print(f"Total sales : {sum(sales_a)}")
    print(f"Average sales : {sum(sales_a)/len(sales_a)}")
    for a, b in zip(sales_a[::1], sales_a[1::1]):
        print (f"Monthly Percentage Change : {(100 * (b - a) / a)}")

#read data 
sales = csv_to_list_of_dicts("sales_data_sample.csv")

#convert data 
sales = sales_data(sales)

#collect sales order by month
#sales_by_month = sorted(sales, key=itemgetter("sales"))
#display result
#pprint(sales_by_month)

#print only sales in single list 
for sale in sales:
    print(f"Month: {sale['MONT_ID']}   Sales: {sale['SALES']}")

#Stats
stats(sales)








