class Customer:
    def __init__(self, customer_id, name, email, phone_number, reservation_history=None):
        if reservation_history is None:
            reservation_history = []
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__reservation_history = reservation_history

    # Getter methods
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_reservation_history(self):
        return self.__reservation_history

    def add_reservation(self, reservation):
        self.__reservation_history.append(reservation)

# Define the Reservation class
class Reservation:
    def __init__(self, reservation_id, room_number, check_in_date, check_out_date, status):
        self.__reservation_id = reservation_id
        self.__room_number = room_number
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status

    # Getter methods
    def get_reservation_id(self):
        return self.__reservation_id

    def get_room_number(self):
        return self.__room_number

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

# Create room objects
room1 = Room(101, "Deluxe", 300, True, 2)

# Create the initial reservation and customer
reservation1 = Reservation("R001", room1.get_room_number(), "2024-09-15", "2024-09-20", "Confirmed")
customer1 = Customer("C001", "Mohammed", "mohammedali@gmail.com", "2334567789")
customer1.add_reservation(reservation1)

# Create additional customers with unique reservation numbers and Gmail emails
customer_abdulla = Customer("R10234", "Abdulla", "abdulla@gmail.com", "3134567891")
customer_mohammed = Customer("R20789", "Mohammed", "mohammed@gmail.com", "3234547892")
customer_ali = Customer("R30156", "Ali", "ali@gmail.com", "326567893")
customer_rashid = Customer("R41562", "Rashid", "rashid@gmail.com", "354845894")
customer_khalid = Customer("R56983", "Khalid", "khalid@gmail.com", "323445895")
customer_zayed = Customer("R67890", "Zayed", "zayed@gmail.com", "345547876")

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

# Function to display customer info
# Function to display customer info, including the name
def display_customer_info(customer, reservation):
    print(f"Customer Name: {customer.get_name()}")
    print(f"Customer Email: {customer.get_email()}")
    print(f"Reservation Number: {reservation.get_reservation_id()}")
    print(f"Room Number: {reservation.get_room_number()}")
    print('*' * 20)  # Custom separator with stars

# Display information for each customer
display_customer_info(customer1, reservation1)
display_customer_info(customer_abdulla, reservation_abdulla)
display_customer_info(customer_mohammed, reservation_mohammed)
display_customer_info(customer_ali, reservation_ali)
display_customer_info(customer_rashid, reservation_rashid)
display_customer_info(customer_khalid, reservation_khalid)
display_customer_info(customer_zayed, reservation_zayed)


# Display information for each customer
display_customer_info(customer1, reservation1)
display_customer_info(customer_abdulla, reservation_abdulla)
display_customer_info(customer_mohammed, reservation_mohammed)
display_customer_info(customer_ali, reservation_ali)
display_customer_info(customer_rashid, reservation_rashid)
display_customer_info(customer_khalid, reservation_khalid)
display_customer_info(customer_zayed, reservation_zayed)
