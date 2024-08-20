import csv

#path to the CSV file
file_path: str = 'example.csv'

#Initialize an empty list to store the data
dados: list = []

with open(file_path, mode='r', encoding='utf-8') as file:
    #create a CSV reader object 
    read_csv = csv.DictReader(file)

    #iterate through the CSV file rows
    for row in read_csv:
        #add each row(a dictionary) to the data list
        dados.append(row)

#print the csv data
print(dados)

