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
    def __init__(self, parkingSpaces, ticketNum, currentTicket):
        self.parkingSpaces = parkingSpaces
        self.ticketNum = ticketNum 
        self.currentTicket = currentTicket
    """
     Garage() expects three arguments:
        parkingSpaces = list
        tickets = int
        currentTicket = dict
    """

    def takeTicket(self):
        if self.ticketNum == 0:
            print("No available space left")

        else:
            spot = int(1)
            while spot in self.currentTicket:
                spot = spot + int(1)
            self.currentTicket[spot] = False
            self.ticketNum -= int(1)
            print(f"This ticket is only valid for spot number {spot}.")


    def payForTicket(self, ticketNum=''):
        if ticketNum != '':
            ticket = ticketNum
        else:
            ticket = int(input("What is your ticket number?"))
        while True:
            if ticket not in self.currentTicket:
                print("That is not a valid ticket number. Try again.")
                continue
            else:
                payment = input("How do you want to pay? Cash or Card?").lower()
                if payment = "cash" or payment = "card"
                    print(f"Please input {payment}")
                    self.currentTicket[ticket] = True
                    print("Thank you for paying. \nYou have 15 minutes to leave the parking area.")
                    return ticketNum
                    break
                else:
                    print(f"We do not accept {payment}. \nPlease choose another form of payment.")
          

    def leaveGarage(self):
        ticketNum = int(input("What is your ticket number?"))
        while ticketNum in self.currentTicket:
            paid = self.currentTicket[ticketNum]
            if paid != True:
                print("This ticket has not been paid.")
                self.payForTicket(ticketNum) #Can we pass on the ticket number?
                continue
            if paid == True:
                print("Thank you. Have nice date")
                self.ticketNum +=1
                del self.currentTicket[ticketNum]
                continue

def capacity(nums):
    spots = []
    for num in range(1, (nums + 1)):
        spots.append(num)
    return spots
    
def open(cap):
    spaces = capacity(cap)
    start = Garage(spaces, cap, {})
    cars = int(0)
    while True:
        arrive = input("What do you want to do? Take/Pay/leave? ").lower()
        if arrive == "take":
            start.takeTicket()
            cars += 1
            continue
        if arrive == 'pay':
            start.payForTicket()
            continue
        if arrive == 'leave':
            start.leaveGarage()
            continue
        if arrive == 'quitquit':
            print(f"The total number of cars today was {cars}.")
            break
        else:
            print("That is not a valid choice. Please try again.")            
            continue        
open(3)