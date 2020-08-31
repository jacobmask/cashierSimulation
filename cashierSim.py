""" File:  project3.py
    Description:  Project 3.  Discrete-Event Simulation of multiple check-out lines.
"""
from priority_queue import PriorityQueue
from priority_queue import PriorityQueueEntry
from queue_text import QueueText
from doubly_linked_deque import Deque
import random

def main():
    # Gather simulation parameters from the user
    numberCashiers = int(input("Enter # of cashiers: "))
    simulationLength = int(input("Enter simulation length (in minutes): "))
    probabilityOfArrival = float(input("Enter probability of customer arrival each minute (0 to 1): "))
    averageCustomerTime = int(input("Enter average # minutes for a customer: "))
    openNewLaneThreshold = int(input("Enter a line amount for the shortest line should be at for a new register to be opened: "))
    maxRegisters = int(input("Max amount of registers in store: "))
    # Set-up data structures needed by the simulation
    
    # holds cashier-idle events "sorted" by event time containing value of cashier # going idle
    cashierIdleEventQueue = PriorityQueue()

    # parallel lists (i.e., index 0 of each list comprises state of cashier 0, etc.) to
    # store the state of all cashiers:  
    customersServedByCashierList = []  # number of customers served by each cashier
    cashierIdleList = []               # whether the cashier is idle (True) or busy (False)
    checkOutLines = []                 # FIFO queue to hold waiting customers in cashier's
                                       # check-out line. Holds a customer's check-out duration
    global totalLineLength
    totalLineLength = []


    # for each cashier set-up their initial state
    for cashier in range(numberCashiers):
        checkOutLines.append(Deque())           # create empty queue for each cashier
        cashierIdleList.append(True)            # each cashiers initially idle
        customersServedByCashierList.append(0)  # tracks # customers served per cashier
        totalLineLength.append(0)

    # run simulation for each minute
    for clock in range(simulationLength):
        # see if a customer arrives and add them to the shortest line if they do
        if customerArrived(probabilityOfArrival):
            addCustomerToShortestLine(checkOutLines, averageCustomerTime, clock)
            numberCashiers = openNewRegister(checkOutLines, openNewLaneThreshold, cashierIdleList, customersServedByCashierList, maxRegisters, numberCashiers)
        # check to see if any cashiers become idle
        updateCashiersState(clock, cashierIdleList, cashierIdleEventQueue,
                           customersServedByCashierList)
        # start next customers if cashier is idle
        startCustomersAtIdleCashiers(clock, checkOutLines, cashierIdleList,
                                    cashierIdleEventQueue)
    printSimulationSummary(checkOutLines, customersServedByCashierList)

def customerArrived(probabilityOfArrival):
    """ Returns a Boolean indicating whether a customer arrives at check-out lines
        within the current minute randomly based on the probabilityOfArrival. """
    randomValue = random.random()  # random float in range [0,1)
    if randomValue < probabilityOfArrival:
        return True
    else:
        return False
    
def addCustomerToShortestLine(checkOutLines, averageCustomerTime, clock):
    """ Determines the duration of the arriving customer's check-out time, then
        adds the customer to the rear of the shortest check-out line. """
    customerClock = clock
    checkOutDuration = random.randint(1, round(2*averageCustomerTime))
    smallestLine = determineSmallestLine(checkOutLines)
    checkOutLines[smallestLine].addRear(checkOutDuration, customerClock)
    totalLineLength[smallestLine] += checkOutDuration
            
def determineSmallestLine(checkOutLines):
    """ Returns the cashier # with the fewest customers in their check-out line. """
    smallestLine = 0
    for line in range(1, len(checkOutLines)):
        if checkOutLines[line].size() < checkOutLines[smallestLine].size():
            smallestLine = line
        elif totalLineLength[line] == min(totalLineLength):
            smallestLine = line
    return smallestLine
    
def updateCashiersState(clock, cashierIdleList, cashierIdleEventQueue,
                        customersServedByCashierList):
    """ Check whether cashiers become idle in this clock tick, and update their
        state if they do. """
    while not cashierIdleEventQueue.isEmpty() and cashierIdleEventQueue.peek().getPriority() <= clock:
        cashierGoingIdle = cashierIdleEventQueue.dequeue().getValue()
        cashierIdleList[cashierGoingIdle] = True
        customersServedByCashierList[cashierGoingIdle] += 1
        #print("Cashier", cashierGoingIdle, "going idle at time", clock)

def startCustomersAtIdleCashiers(clock, checkOutLines, cashierIdleList, cashierIdleEventQueue):
    """ Start the next customer at cashiers which are idle and have someone in their
        check-out line. """
    global totalWait
    totalWait = 0
    for cashier in range(len(cashierIdleList)):
        if cashierIdleList[cashier] and not checkOutLines[cashier].isEmpty():
            customerServeTime, endClock = checkOutLines[cashier].removeRear()

            totalWait += endClock
            cashierIdleList[cashier] = False
            # schedule future event for when cashier will go idle
            cashierIdleEventQueue.enqueue(PriorityQueueEntry(clock+customerServeTime+1,cashier))

def openNewRegister(checkOutLines, openNewLaneThreshold, cashierIdleList, customersServedByCashierList, maxRegisters, numberCashiers):
    """Opens new register and adds register to list if the shortest line meets the length threshold"""
    smallestLine = determineSmallestLine(checkOutLines)
    if checkOutLines[smallestLine].size() >= openNewLaneThreshold and numberCashiers < maxRegisters:
        checkOutLines.append(Deque())       # create empty queue for each cashier
        cashierIdleList.append(True)            # each cashiers initially idle
        customersServedByCashierList.append(0)  # tracks # customers served per cashier
        numberCashiers += 1
        totalLineLength.append(0)
    return numberCashiers


            
def printSimulationSummary(checkOutLines, customersServedByCashierList):
    """ For each cashier, prints the # of customers served and the # of customers
        still waiting in their check-out line when the simulation ends. """
    totalCustomers = 0
    averageWait = 0
    for cashier in range(len(checkOutLines)):
        print("\nCashier", cashier, "checked out", customersServedByCashierList[cashier],
              "customers with", checkOutLines[cashier].size(),
              "customers in their line at end of simulation.")
        totalCustomers += customersServedByCashierList[cashier]
    averageWait = totalWait/totalCustomers
    
    print("The average wait was", int(averageWait), "minute(s), for a total of", totalCustomers, "customer(s)")
        
main()  # start simulation running
