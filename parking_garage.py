# Your parking gargage class should have the following methods:
# -takeTicket
#    - This should decrease the amount of tickets available by 1
#    - This should decrease the amount of parkingSpaces available by 1
# -payForParking
#    - Display an input that waits for an amount from the user and store it in a variable
#    - If the payment variable is not empty then ->  display a message to the user that their ticket has been paid and they have 15mins to leave
#    - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
#    - If the ticket has been paid, display a message of "Thank You, have a nice day"
#    - If the ticket has not been paid, display an input prompt for payment
#       - Once paid, display message "Thank you, have a nice day!"
#    - Update parkingSpaces list to increase by 1
#    - Update tickets list to increase by 1

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# When the project is completed, commit the final changes, sync all pull requests, and each member should submit their respective GitHub links(though the code in each should be the same)

class Garage():
    def __init__(self, parkingSpaces, tickets, currentTicket):
        self.parkingSpaces = parkingSpaces
        self.tickets = tickets 
        self.currentTicket = currentTicket

    def takeTicket(self):
        if self.parkingSpaces = 0:
            print("No available space left")
        else:
            space_tot = self.parkingSpaces - 1
            ticket_tot = self.tickets + 1
            self.parkingSpaces = space_tot
            self.tickets = ticket_tot
            currentTicket[] = "unpaid"
    def payForTicket(self):

    def leaveGarage(self):
        ticketNum = int(input("What is your ticket number?"))
        paid = self.currentTicket[ticketNum]
        while ticketNum in self.currentTicket.items():


        


def open():
    start = Garage(60, 0, {})

    while True:
        arrive = input("What do you want to do? Take/Pay/leave? ").lower()
        if arrive == "take":
            start.takeTicket()
            continue
        
open()