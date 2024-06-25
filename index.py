
class ParkingGarage:
    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets > 0 and self.parking_spaces > 0:
            self.tickets -= 1
            self.parking_spaces -= 1
            self.current_ticket[self.tickets] = {'paid': False}
            print("Please take your ticket. Enjoy your parking!")

    def pay_for_parking(self):
        ticket_num = int(input("Please enter your ticket number: "))
        if ticket_num in self.current_ticket.keys():
            payment = input("Please enter your payment amount: ")
            if payment:
                self.current_ticket[ticket_num]['paid'] = True
                print("Payment successful. You have 15 minutes to leave.")
            else:
                print("Payment not entered. Payment failed.")
        else:
            print("Ticket number not found.")

    def leave_garage(self):
        ticket_num = int(input("Please enter your ticket number: "))
        if ticket_num in self.current_ticket.keys():
            if self.current_ticket[ticket_num]['paid']:
                print("Thank you for your payment. Have a nice day!")
                self.parking_spaces += 1
                self.tickets += 1
                del self.current_ticket[ticket_num]
            else:
                payment = input("Please pay for parking: ")
                if payment:
                    self.current_ticket[ticket_num]['paid'] = True
                    print("Payment successful. Have a nice day!")
                    self.parking_spaces += 1
                    self.tickets += 1
                else:
                    print("Payment not entered. Exiting.")
        else:
            print("Ticket number not found.")

# Testing the ParkingGarage class
tickets_available = 10
parking_spaces_available = 10

garage = ParkingGarage(tickets_available, parking_spaces_available)

while True:
    print("\nWelcome to the Parking Garage")
    print("1. Take a ticket")
    print("2. Pay for parking")
    print("3. Leave the garage")
    print("4. Quit")
    
    choice = input("Please select an option (1/2/3/4): ")

    if choice == '1':
        garage.take_ticket()
    elif choice == '2':
        garage.pay_for_parking()
    elif choice == '3':
        garage.leave_garage()
    elif choice == '4':
        print("Thank you for using the parking garage. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
Explanation:
Class Definition: The ParkingGarage class is defined with attributes (tickets, parking_spaces, current_ticket) and methods (take_ticket, pay_for_parking, leave_garage).

Initialization (__init__): Initializes the parking garage with available tickets and parking spaces. current_ticket dictionary keeps track of current tickets and their payment status.

Methods:

take_ticket: Decreases available tickets and parking spaces when a ticket is taken.
pay_for_parking: Allows users to pay for their parking ticket. Updates the payment status in current_ticket.
leave_garage: Allows users to leave the garage. Checks if the ticket is paid, collects payment if not paid, and updates available tickets and parking spaces.
Loop: The while loop allows the user to interact with the parking garage until they choose to quit (choice == '4').

User Interaction: Each option (1, 2, 3, 4) corresponds to a method of the ParkingGarage class, providing a full user experience for managing parking.

This implementation demonstrates basic principles of OOP in Python, including class instantiation (garage = ParkingGarage()), method definitions (def take_ticket(self), etc.), and attribute management (self.tickets, self.parking_spaces, self.current_ticket).