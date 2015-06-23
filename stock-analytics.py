from yahoo_finance import Share
from pprint import pprint
from csv import DictWriter
import json

stock = input("Please enter a stock symbool to get info: ")

stock = Share(stock)
a = input("Enter analytics start date (YYYY-MM-DD): ")
b = input("Enter analytics end date (YYYY-MM-DD): ")
print("Current price: ",stock.get_price())
data = stock.get_historical(a, b)
pprint(data)

json_str = json.dumps(data)
with open('data.json', 'w') as f:
     json.dump(data, f)

dicts = json.loads(json_str)
name = input("Enter a name for the saved .csv file: ")
savedfile = open(name+".csv", "w")
writer = DictWriter(savedfile, dicts[0].keys())
writer.writeheader()
writer.writerows(dicts)
savedfile.close()

#Written for the Florida Polytechnic Big Data Analytics Lab
#By Jean-Patrice Jean-Louis
