from datetime import datetime    ### for time
from datetime import timedelta  ### for time addition
import os  #to use 'clear()'
def clear():#to use 'clear()'
    os.system( 'cls' )

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
            print("No available space left. Sorry.")            
        else:
            spot = int(1)
            while spot in self.currentTicket:
                spot = spot + int(1)
            self.currentTicket[spot] = False
            self.ticketNum -= int(1)
            print(f"This ticket is only valid for spot number {spot}.")



    def payForTicket(self, ticketNum=''):
        if ticketNum != '':      ###### Allows for the carry over of ticket number from the 'leaveGarage' method, it will also feed back into the function and allow people to leave. 
            ticket = ticketNum
        else:
            ticket = int(input("What is your ticket number?"))  ############################################For these inputs it would be nice to: print("That is not a valid number.")

        if ticketNum in self.currentTicket:
            while True:
                if ticket not in self.currentTicket:    #checks to see if the ticket is in the current tickets.
                    print("That is not a valid ticket number. Try again.")
                    ticket = int(input("What is your ticket number?"))
                    continue
                elif self.currentTicket[ticket] == True:  #stops from repeat paying.
                    print("You have already paid.")
                    break
                else:
                    payment = input("How do you want to pay? Cash or Card?").lower()
                    if payment == "cash" or payment == "card":
                        print(f"Please input {payment}")
                        self.currentTicket[ticket] = True   
                        now = datetime.now()       #####Next three lines give the time stamps
                        time = now.strftime("%H:%M:%S")
                        fifteen = datetime.now() + timedelta(minutes=15)
                        print(f"Thank you for paying. \nYou have 15 minutes to leave the parking area. \n\nThe current time is {time}\nYou should be out by {fifteen}\n") ### displays current time and the time they need to leave by.
                        return ticketNum  #Returns value to 'leaveGarage' fo they can leave right away.
                    else:
                        print(f"We do not accept {payment}s. \nPlease choose another form of payment.") ### Error message
        else:
            print("That is not a valid number.")   ### Error message
          

    def leaveGarage(self):
        ticketNum = int(input("What is your ticket number?")) ############################################For these inputs it would be nice to: print("That is not a valid number.")
        if ticketNum in self.currentTicket:  #### checks if they ticket is in currentTickets
            while ticketNum in self.currentTicket:
                paid = self.currentTicket[ticketNum]
                if paid != True:
                    print("This ticket has not been paid.")
                    self.payForTicket(ticketNum) #Can we pass on the ticket number?
                    continue
                if paid == True:
                    print("\nThank you. Have nice day.\n")
                    self.ticketNum +=1
                    del self.currentTicket[ticketNum]
                    continue
                else:
                    print(f"else--Ticket {ticketNum} is not in our system currently.")
                    break
        else:
            print(f"Ticket {ticketNum} is not in our system currently.")


def capacity(nums):
    spots = []
    for num in range(1, (nums + 1)):
        spots.append(num)
    return spots

    
    
    
    
counter = int(0)     ###### Small testing program. gives different return values for 'arrive'
import random      ###### Small testing program. gives different return values for 'arrive'
def rand(counter):     ###### Small testing program. gives different return values for 'arrive'
    counter += 1     ###### Small testing program. gives different return values for 'arrive'
    while counter < 20:     ###### Small testing program. gives different return values for 'arrive'
        num = random.randint(1, 4)     ###### Small testing program. gives different return values for 'arrive'
        if num == 1:     ###### Small testing program. gives different return values for 'arrive'
            return 'take'     ###### Small testing program. gives different return values for 'arrive'
        if num == 2:     ###### Small testing program. gives different return values for 'arrive'
            return 'pay'     ###### Small testing program. gives different return values for 'arrive'
        if num == 3:     ###### Small testing program. gives different return values for 'arrive'
            return 'leave'     ###### Small testing program. gives different return values for 'arrive'
        if num == 4:     ###### Small testing program. gives different return values for 'arrive'
            return "alksdjfnhaesfui"     ###### Small testing program. gives different return values for 'arrive'
    
def open(cap):
    spaces = capacity(cap)
    start = Garage(spaces, cap, {})
    cars = int(0)
    while True:          
        arrive = input("What do you want to do? Take/Pay/leave? ").lower()   #### if you want to use random responses put this before input: rand(counter)#
        clear()
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
            print(f"The total number of cars today was {cars}.")    ###prints total cars for the day.
            break
        else:
            print("That is not a valid choice. Please try again.")             ### Error message
            continue        
open(10)