# Define the Customer class
class Customer:
    def __init__(self, customer_id, name, email, phone_number, reservation_history=None):
        if reservation_history is None:
            reservation_history = []
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__reservation_history = reservation_history

    # Getter and Setter methods
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_reservation_history(self):
        return self.__reservation_history

    def add_reservation(self, reservation):
        self.__reservation_history.append(reservation)

    def cancel_reservation(self, reservation_id):
        for reservation in self.__reservation_history:
            if reservation.get_reservation_id() == reservation_id:
                self.__reservation_history.remove(reservation)
                break

# Define the Reservation class
class Reservation:
    def __init__(self, reservation_id, room_number, check_in_date, check_out_date, status):
        self.__reservation_id = reservation_id
        self.__room_number = room_number
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status

    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def check_availability(self):
        pass

    def modify_reservation(self, new_check_in, new_check_out):
        self.__check_in_date = new_check_in
        self.__check_out_date = new_check_out

    def cancel_reservation(self):
        self.__status = "Cancelled"

# Define the Room class
class Room:
    def __init__(self, room_number, room_type, price, is_available, max_occupancy):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price = price
        self.__is_available = is_available
        self.__max_occupancy = max_occupancy

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def is_room_available(self):
        return self.__is_available

    def set_availability(self, is_available):
        self.__is_available = is_available

    def get_max_occupancy(self):
        return self.__max_occupancy

    def set_max_occupancy(self, max_occupancy):
        self.__max_occupancy = max_occupancy

# Define the Payment class
class Payment:
    def __init__(self, payment_id, payment_date, amount, payment_method, reservation_id):
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__amount = amount
        self.__payment_method = payment_method
        self.__reservation_id = reservation_id

    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_payment_date(self):
        return self.__payment_date

    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def process_payment(self):
        pass

# Create room objects
room1 = Room(101, "Deluxe", 300, True, 2)

# Create the initial reservation and customer
reservation1 = Reservation("R001", room1.get_room_number(), "2024-09-15", "2024-09-20", "Confirmed")
customer1 = Customer("C001", "Mohammed", "mohammedali@gmail.com", "2334567789")
customer1.add_reservation(reservation1)

# Create and process the payment for this reservation
payment1 = Payment("P001", "2024-09-15", 300, "Credit Card", reservation1.get_reservation_id())
payment1.process_payment()

# Create additional customers and reservations
customer_abdulla = Customer("C002", "Abdulla", "abdullahussein.com", "3134567891")
customer_mohammed = Customer("C003", "Mohammed", "mohammedmaalim.com", "3234547892")
customer_ali = Customer("C004", "Ali", "alihassan.com", "326567893")
customer_rashid = Customer("C005", "Rashid", "rashidabdi.com", "354845894")
customer_khalid = Customer("C006", "Khalid", "khalidabdullah.com", "323445895")
customer_zayed = Customer("C007", "Zayed", "zayedkhalid.com", "345547876")

# Create reservations for each customer
reservation_abdulla = Reservation("R002", 102, "2024-10-01", "2024-10-05", "Confirmed")
reservation_mohammed = Reservation("R003", 103, "2024-10-02", "2024-10-06", "Confirmed")
reservation_ali = Reservation("R004", 104, "2024-10-03", "2024-10-07", "Confirmed")
reservation_rashid = Reservation("R005", 105, "2024-10-04", "2024-10-08", "Confirmed")
reservation_khalid = Reservation("R006", 106, "2024-10-05", "2024-10-09", "Confirmed")
reservation_zayed = Reservation("R007", 107, "2024-10-06", "2024-10-10", "Confirmed")

# Add reservations to the customers
customer_abdulla.add_reservation(reservation_abdulla)
customer_mohammed.add_reservation(reservation_mohammed)
customer_ali.add_reservation(reservation_ali)
customer_rashid.add_reservation(reservation_rashid)
customer_khalid.add_reservation(reservation_khalid)
customer_zayed.add_reservation(reservation_zayed)

# Create and process payments for each reservation
payment_abdulla = Payment("P002", "2024-09-30", 500, "Credit Card", reservation_abdulla.get_reservation_id())
payment_mohammed = Payment("P003", "2024-09-30", 700, "Credit Card", reservation_mohammed.get_reservation_id())
payment_ali = Payment("P004", "2024-09-30", 700, "Credit Card", reservation_ali.get_reservation_id())
payment_rashid = Payment("P005", "2024-09-30", 800, "Credit Card", reservation_rashid.get_reservation_id())
payment_khalid = Payment("P006", "2024-09-30", 600, "Credit Card", reservation_khalid.get_reservation_id())
payment_zayed = Payment("P007", "2024-09-30", 900, "Credit Card", reservation_zayed.get_reservation_id())

# Process payments
payment_abdulla.process_payment()
payment_mohammed.process_payment()
payment_ali.process_payment()
payment_rashid.process_payment()
payment_khalid.process_payment()
payment_zayed.process_payment()

# Display information for each customer
print(f"Customer: {customer1.get_name()}, Reservation: {reservation1.get_room_number()}, Payment: {payment1.get_amount()}")
print(f"Customer: {customer_abdulla.get_name()}, Reservation: {reservation_abdulla.get_room_number()}, Payment: {payment_abdulla.get_amount()}")
print(f"Customer: {customer_mohammed.get_name()}, Reservation: {reservation_mohammed.get_room_number()}, Payment: {payment_mohammed.get_amount()}")
print(f"Customer: {customer_ali.get_name()}, Reservation: {reservation_ali.get_room_number()}, Payment: {payment_ali.get_amount()}")
print(f"Customer: {customer_rashid.get_name()}, Reservation: {reservation_rashid.get_room_number()}, Payment: {payment_rashid.get_amount()}")
print(f"Customer: {customer_khalid.get_name()}, Reservation: {reservation_khalid.get_room_number()}, Payment: {payment_khalid.get_amount()}")
print(f"Customer: {customer_zayed.get_name()}, Reservation: {reservation_zayed.get_room_number()}, Payment: {payment_zayed.get_amount()}")
