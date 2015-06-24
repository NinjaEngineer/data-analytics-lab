#Written for the Florida Polytechnic Big Data Analytics Lab
#By Jean-Patrice Jean-Louis

from yahoo_finance import Share
from csv import DictWriter
import json

symbol = input("Please enter a symbol symbol to get info: ")
startDate = input("Enter analytics start date (YYYY-MM-DD): ")
endDate = input("Enter analytics end date (YYYY-MM-DD): ")
csvFile = input("Enter a name for the saved .csv file, omitting the .csv ") + ".csv"

# def getstockjson():
symbol = Share(symbol)
data = symbol.get_historical(startDate, endDate)
json_str = json.dumps(data)
with open('data.json', 'w') as f:
    json.dump(data, f)
dicts = json.loads(json_str)


saveFile = open(csvFile, "w")
writer = DictWriter(saveFile, dicts[0].keys(), lineterminator='\n')
writer.writeheader()
writer.writerows(dicts)
saveFile.close()

#
# def main():
#     getstockjson()
#     saveStockCsv()
#
# if __name__ == "__main__":
#     main()
