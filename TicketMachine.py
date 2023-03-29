import datetime
import random
import matplotlib.pyplot as plt
import sys

States=[0,1,2,3,4,5]
Prices=[0, 400, 300, 200, 100, 50]
#Dictionary from 1 to nine all initialized as 0
counterscounter=[0,0,0,0,0,0,0,0]

TicketQuantity = {i: 0 for i in range(1, 31)}
ticketnumber=0


def TicketType():
    print("Select the type of the ticket:\n     1. Repair Ticket\n     2. Delivery Ticket\n     p. Show Plot\n     map. Map of Counters ")
    typeofticket= input()
    if typeofticket == "1" or typeofticket == "2":
        return typeofticket
    if typeofticket == "p":
        TicketPlotCounter()
    if typeofticket == "map":
        Counterplot(counter, counterscounter)
    else: 
        return "Invalid Input"


def Ticketfill(ticketnumber):

    ticketnumber +=1 
    time= datetime.datetime.now()       ##returns the present time
    fill_time=time.replace(microsecond=0)
    print("Ticket emission time: "+ str(fill_time))
    print("Ticket number: " + str(ticketnumber))
    return ticketnumber
    

#Functions that return the information of the answered tickets
def TicketAnswered(ticketnumber):
    typeofticket= TicketType()
    print("Counter value: ",counter)
    counterscounter[counter]+=1
    time= datetime.datetime.now()
    time_answer= time.replace(microsecond=0)
    print("Ticket " + str(ticketnumber) + " answer time: "+ str(time_answer))
    print("Answering Counter. "+str(counter))

    equipment_state_str = ""  # Initialize the variable with an empty string


    if typeofticket =="1":

        # Get the current day of the month using datetime.datetime.now()
        current_day = datetime.datetime.now().day
        # Update the dictionary with the count for the current day
        TicketQuantity[current_day] += 1

        equipment= input("Equipment to be fixed: ")
        equipment_problem= input("Problem with the equipment: ")
        observations= input("Any observations to be added? (Please type 'No' if you have no obstervations to make): ")
        
        print("Equipment: " + str(equipment))
        print("Equipment's problem: " + str(equipment_problem))
        print("Observations: " + str(observations))

    elif typeofticket == "2":
        # Get the current day of the month using datetime.datetime.now()
        current_day = datetime.datetime.now().day
        # Update the dictionary with the count for the current day
        TicketQuantity[current_day] += 1
        TicketQuantity[4] =5
        TicketQuantity[10]=10

        print("0. The equipment is beyond salvaging. Should be handed for recycling.")
        print("1. The equipment rarely shows to work effectivelly. Very difficult to fix")
        print("2. The equipment demonstrates clear faults in its functioning. Rather difficult solution")
        print("3. The equipment's performance is sometimes lacking. Should be solvable")
        print("4. The equipment is still in very good shape. Only a small change should be required")
        print("5. The equipment is in near perfect state. Minor inconvineance")

        equipment_state_str= input("Enter the equipment's state: ")
        try:
            equipment_state= int(equipment_state_str)
            if equipment_state in States:
             price_index = States.index(equipment_state)
             price = Prices[price_index]
             print("The price for a service of level "+ str(equipment_state)+ " is "+ str(price) + "€")
            else:
                print("Invalid Input: Please enter a valid equipment state (0-5)")
        except ValueError:
            print("Invalid Input: Please enter a number")
    return counter
    return counterscounter


def TicketPlotCounter():

    plt.bar(TicketQuantity.keys(), TicketQuantity.values())
    plt.xlabel('Day of the Month')
    plt.ylabel('Number of Tickets')
    plt.xticks(list(TicketQuantity.keys()))
    plt.show()
    sys.exit()
    
def Counterplot(counter, counterscounter):
    plt.bar(range(1, 8), counterscounter, width=0.4)
    plt.xlabel("Counter")
    plt.ylabel("Number of tickets answered")
    plt.xticks(range(1, 9))
    plt.show()
    sys.exit()




if __name__ == "__main__":
    
    while True:
        
        while input("Press enter to start...") != "\n":
         counter=random.randrange(1,9)
         ticketnumber= Ticketfill(ticketnumber)
         TicketAnswered(ticketnumber)
        
        
        
        