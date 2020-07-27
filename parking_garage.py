import datetime
from datetime import datetime    ### for time
from datetime import timedelta  ### for time addition
import os  #to use 'clear()'
def clear():#to use 'clear()'
    os.system( 'cls' )

class Garage():
    def __init__(self, parkingSpaces, ticketNum, closeTime, currentTicket):
        self.parkingSpaces = parkingSpaces
        self.ticketNum = int(ticketNum) 
        self.closeTime = closeTime
        self.currentTicket = currentTicket
    """
     Garage() expects three arguments:
        parkingSpaces = list
        tickets = int
        closingTime = datetime()
        currentTicket = dict
    """


    def takeTicket(self,cars):
        now = datetime.now()       #####Next three lines give the time stamps  
        if self.ticketNum == 0:
            print("No available space left. Sorry.")            
        else:
            spot = int(1)
            while spot in self.currentTicket:
                spot = spot + int(1)
            self.currentTicket[spot] = False
            self.ticketNum -= int(1)            
            print(f"This ticket is only valid for parking spot {spot}.\nThe time now is {now}. \nThe garage closes at {self.closeTime}. Please make sure to have your vehicle out before then. Otherwise you will be charged an over night fee.")
            cars += 1
            return cars



    def payForTicket(self, ticketNum=''):
        while ticketNum == '':
            ticketNum = int(input("What is your parking spot number?"))  ############################################For these inputs it would be nice to: print("That is not a valid number.")
        ticket = int(ticketNum)
        # try ticket in self.currentTicket.keys:

        now = datetime.now()       #####Next three lines give the time stamps
        time = now.strftime("%H:%M")
        # close = self.closeTime - time #only works if closeTime function is working.
        # print(close)
        while True:
            if ticket not in self.currentTicket:    #checks to see if the ticket is in the current tickets.
                print("That is not a valid parking spot number. Try again.")
                ticket = int(input("What is your parking spot number?"))
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
                    # if fifteen > close:
                    #     print(f"Thank you for paying. \nYou have 15 minutes to leave the parking area. \n\nThe current time is {time}\nYou should be out by {fifteen}\n") ### displays current time and the time they need to leave by.
                    #     return ticketNum  #Returns value to 'leaveGarage' fo they can leave right away.

                    # else:
                    print(f"Thank you for paying. \nYou have 15 minutes to leave the parking area. \n\nThe current time is {time}\nYou should be out by {fifteen}\n") ### displays current time and the time they need to leave by.
                    return ticketNum  #Returns value to 'leaveGarage' fo they can leave right away.
                else:
                    print(f"We do not accept {payment}s. \nPlease choose another form of payment.") ### Error message
        # except:
        #     print("That is not a valid number.")   ### Error message
          

    def leaveGarage(self):
        ticketNum = int(input("What was your parking spot number?")) ############################################For these inputs it would be nice to: print("That is not a valid number.")
        if ticketNum in self.currentTicket:  #### checks if they ticket is in currentTickets
            while ticketNum in self.currentTicket:
                paid = self.currentTicket[ticketNum]
                if paid != True:
                    print("This spot has not been paid.")
                    self.payForTicket(ticketNum) #Can we pass on the ticket number?
                    continue
                if paid == True:
                    print("\nThank you. Have nice day.\n")
                    self.ticketNum +=1
                    del self.currentTicket[ticketNum]
                    continue
                else:
                    print(f"else--Parking spot {ticketNum} is not indacated as in use in our system currently.")
                    break
        else:
            print(f"Parking spot {ticketNum} is not indacated as in use in our system currently.")


def capacity(nums):
    """
    This fn creates a list that is the total number of parking spots.
     -expects the capacity number from the original call of 'open()' fn
    """
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
    """
    This function expects one value:
        cap = an Int() that is the total number of parking spaces in the parking garage.
    """
    closeTime = int(2200)
    # now = datetime.now()       #####Next three lines give the time stamps
    # time = now.strftime("%H:%M:%S")

    # try:
    #     closeTime = datetime.datetime.strptime(raw_input('specify closing 24h-time in HHMM format: '), "%H%M")
    #     print closeTime.strftime( "%H%M")
    # except:
    #     print "Please enter correct time in HHMM format"
    # print(closeTime)
    spaces = capacity(cap)
    start = Garage(spaces, cap, closeTime, {}) #only works if we can get closeTime working.
    cars = int(0)
    while True:          
        arrive = input("What do you want to do? Take/Pay/leave? ").lower()   #### if you want to use random responses put this before input: rand(counter)#
        clear()
        if arrive == "take":
            start.takeTicket(cars)
            
            continue
        if arrive == 'pay':
            start.payForTicket()
            continue
        if arrive == 'leave':
            start.leaveGarage()
            continue
        if arrive == 'quitquit':
            print(f"The total number of cars today was {cars}.")    ###For Employee at closing: prints total cars for the day.
            break
        else:
            print("That is not a valid choice. Please try again.")             ### Error message
            continue        
open(10)