'''
#formate....
import csv
filename = "demo.csv"

fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [ ['Nikhil', 'COE', '0' , '0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']]

with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(rows)


fields = []
rows = []

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row)

for i in fields:
	print(i)
print('rows', '*'*30)

for i in rows:
	print(i)

import pandas as pd 
df = pd.read_csv("demo.csv")  
df.loc[3, 'Name'] = 'shiv kumar'

df.to_csv("demo.csv", index=False) 


import pandas as pd
df = pd.read_csv(filename)
df = df.drop(df.index[2])
'''
#project implimentation...

import csv
import pandas as pd
filename = 'create.csv'

total_rooms=[101,102,103,104,105]
available_room=[]
allocated_room=[]

def find_index():
    room_no = input('Enter room no here: ')
    with open(filename, 'r') as fh:
        csvreader = csv.reader(fh)
        fields = next(csvreader)
        index = 0
        for records in csvreader:
            if records:
                if records[0] == room_no:
                    return index
                index += 1

def check_rooms():
    global available_rooms, allocated_rooms
    with open(filename, 'r') as fh:
        csvreader = csv.reader(fh)
        fields = next(csvreader)
        allocated_rooms = [int(records[0]) for records in csvreader if records]
        available_rooms = list(set(total_rooms) ^ set(allocated_rooms))

def new_customer():
    if available_rooms:
        room_no = available_rooms.pop()
        name = input('Enter name here: ')
        contact = int(input('Contact: '))
        days = int(input('Enter number of stays: '))
        bill = days * 800
        fields = [room_no, name, contact, bill]
        with open(filename, 'a') as fh:
            csvwriter = csv.writer(fh)
            csvwriter.writerow(fields)
        print(f'Hi {name}, here is your key of room no {room_no}')
    else:
        print('No rooms available....')

def show_all_cust():
    with open(filename, 'r') as fh:
        csvreader = csv.reader(fh)
        fields = next(csvreader)
        for records in csvreader:
            if records:
                print(f'{records[1]} is staying in room no {records[0]} and their total bill is {records[3]}')

def update_customer():
    index = find_index()
    ch = int(input('What do you want to update:\n' \
                   '1. Name\n' \
                   '2. Contact\n'))
    if ch == 1:
        field = 'name'
        change = input('Enter new name: ')
    elif ch == 2:
        field = 'contact'
        change = int(input('Enter new contact: '))
    else:
        print('Invalid choice')
        return
    
    df = pd.read_csv(filename)
    df.loc[index, field] = change
    df.to_csv(filename, index=False)
    print('Updated')

def delete_customer():
    index1 = find_index()
    df = pd.read_csv(filename)
    df = df.drop(df.index[index1])
    df.to_csv(filename, index=False)
    print('Deleted')

def exist_customer():
    print("Customer exists......")

while True:
    ch = int(input('Enter choice:\n' \
                   '1. New Customer\n' \
                   '2. Show All Customers\n' \
                   '3. Update Contact\n' \
                   '4. Delete\n' \
                   '5. Exist'))

    match ch:
        case 1:
            check_rooms()
            new_customer()
        case 2:
            show_all_cust()
        case 3:
            update_customer()
        case 4:
            delete_customer()
        case 5:
            exist_customer()
            break
        case _:
            print("Invalid choice....")
                





























