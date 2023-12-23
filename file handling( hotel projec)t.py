#hotel project by using file handling.....

from datetime import datetime
class Hotel:
    def __init__(self, name, room_no, mob_no, room_bill=0, resto_bill=0, gaming_bill=0, laundry_bill=0):
        self.name = name
        self.mob_no = mob_no
        self.room_no = room_no
        self.room_bill = room_bill
        self.gaming_bill = gaming_bill
        self.laundry_bill = laundry_bill
        self.resto_bill = resto_bill

    def __str__(self):
        return f'Customer name = {self.name}\n'\
               f'Mobile Number = {self.mob_no}\n'\
               f'Room Number = {self.room_no}\n'\
               f'Room Bill = {self.room_bill}\n'\
               f'Gaming Bill = {self.gaming_bill}\n'\
               f'Laundry Bill = {self.laundry_bill}\n'\
               f'Resto_bill = {self.resto_bill}\n'
    
available_room = [101, 102, 103]
allocated_rooms = []
customer_list = []

def new_customer():
    print('*********Welcome*********')
    
    if available_room:
        room_no = available_room.pop()
        allocated_rooms.append(room_no)
        name = input('Enter your name here:')
        mobile_no = int(input('Enter mobile number here:'))
        number_of_days = int(input('Enter no.of days:'))     
        customer = Hotel(name, room_no, mobile_no, room_bill=number_of_days*800)
        print(f'Hi {name}, here is your key of room no {room_no}')
        customer_list.append(customer)
    else:
        print('Sorry no rooms are available')
        
def existing_customer():
    ch = int(input(('****** SERVICES ********\n'\
                    '1.RESTAURANT\n'\
                    '2.gaming\n'\
                    '3.loundary\n')))
    customer_room_no = int(input('Plz Enter your room number here:'))
    for i in customer_list:
        if i.room_no == customer_room_no:
             break
    cust = i
    
    if ch == 1:
        ch1 = int(input('***Menu***\n'\
                          '1.Tea    --> 10rs\n'\
                          '2.Lunch  --> 120rs\n'\
                          '3.Exit'))
        if ch1 == 1:
             quantity = int(input('How many number of teas:'))
             cust.resto_bill += quantity*10
             
        elif ch1 == 2:
             quantity = int(input('How many number of lunch:'))
             cust.resto_bill += quantity*120
             
        elif ch1 == 3:
            print('Exit from restro')

    if ch == 2:
        ch2 = int(input('***gamesmenu***\n'\
                        '1.chess\n'\
                        '2.bikeride\n'\
                        '3.ludo\n'\
                        '4.exit\n'))
        if ch2 ==1:
            quantity=int(input("How many attempt of chess:"))
            cust.resto_bill += quantity*20

        elif ch2 ==2:
            quantity=int(input("How many attempt of bikeride:"))
            cust.resto_bill += quantity*30

        elif ch2 ==3:
            quantity=int(input("How many attempt of ludo:"))
            cust.resto_bill += quantity*50

        elif ch2==4:
            print('Exit from games')
            
            
    if ch == 3:
        ch3 = int(input("***laundary***\n"\
                        "1.pants\n"\
                        "2.shirts\n"\
                        "3.dress\n"\
                        "4.exit\n"))
        if ch3 ==1:
            quantity=int(input("How many pants:"))
            cust.resto_bill += quantity*10

        elif ch3 ==2:
            quantity=int(input("How many shirts:"))
            cust.resto_bill += quantity*10

        elif ch3 ==3:
            quantity=int(input("How many dress:"))
            cust.resto_bill += quantity*20

        elif ch4==4:
            print('Exit from loundary')
            
                                
          
                    
def customer_details():
    for i in customer_list:
        print(i)


def billing_checkout():
    customer_room_no = int(input('Plz Enter your room number here:'))
    for i in customer_list:
        if i.room_no == customer_room_no:
             break
    cust = i
    total_bill = cust.room_bill + cust.gaming_bill + cust.laundry_bill + cust.resto_bill
    print(f'Your total bill is {total_bill}')
    allocated_rooms.remove(customer_room_no)
    available_room.append(customer_room_no)
    customer_list.remove(i)
    print('Thanks for visting our Hotel')
    

fh=open("logfile12.txt","a")
fh.write(f"\n{datetime.now()}: user started hotel project")
        
while True:
    ch=int(input("enter your choice:\n"\
                 '1. New Customer \n'\
                 '2. Existing Customer\n'\
                 '3. Customer Details \n'\
                 '4. Billing and Checkout\n'\
                 '5.exit'))
    match ch:
        case 1:
            new_customer()
            fh.write(f"\n{datetime.now()}:user perform new_customer details")
        case 2:
            existing_customer()
            fh.write(f"\n{datetime.now()}:user perform existing_customer details")
        case 3:
            customer_details()
            fh.write(f"\n{datetime.now()}:user perform customer_customer details")
        case 4:
            billing_checkout()
            fh.write(f"\n{datetime.now()}:user perform billing_customer details")
        case 5:
            print("exsisting......")
            fh.write(f"\n{datetime.now()}:user perform existing details")
            break
        case _:
            print("invalid choice....")
            fh.write(f"\n{datetime.now()}:user perform invalid choice detail")
fh.close()
