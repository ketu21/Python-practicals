import random

class jobscheduling():
    """this class is to handle various functions of the scheduling algorithms"""
    process_list = []       #a list of list to store the processes
    total_processes = 0     #variable to keep track of total number of processes
    total_time = 0          #variable to keep track of total time that CPU will need to processes all the processes
    time_slice = 5          #time slice for round robin by default it is set to 5
    def __init__(self):
        """this is constructor that initializes the variables """
        self.process_list = self.readfile()             #read the list from a file
        self.process_list.sort(key=lambda x: x[1])      # sort the processes according to arrival time
        self.time()                                     #calculate the total time

    def rand_generate(self, n):
        """this function creates random processes with arival time and burst time """
        #the number of processes to be created is passes as argument by taking the user's input
        list1 = []
        list2 = []
        self.total_processes = 0
        for x in range(0,n):
            #this loop generates random integer twice  and appends it to list1
            #so list 1 will contain total 3 integers in which 1 is process id 2 is arival time
            # and 3 is burst time and then the list1 is appended to list2 which contains list of list for storing processes
            list1.append(x)
            list1.append(random.randint(1, 20))         #apend random int to list 1 which is >1 and <20
            list1.append(random.randint(1,30))          #apend random int to list 1 which is >1 and <30
            list2.append(list1)                         #append the list2 to list2
            self.total_processes += 1                   #updates total number of processes
            list1 = []
        self.process_list = list2                       #assign list2 to processes_list variable
        self.process_list.sort(key=lambda x: x[1])      # sort the processes according to arrival time
        print(self.process_list)

    def readfile(self):
        """this function reads the processes from the file and stores this in the respective variables"""
        with open('processes.txt') as f:        #loop file pointer till the end of file
            list = []
            for line in f:                      #read by each line from the file
                list.append([int(x) for x in line.split()])     #this part seperates the id, arival time and burst time from the line read from file
                self.total_processes += 1                       #update total processes number
        return(list)

    def time(self):
        """this function is to calculate total time required to process all the processes"""
        #this can be achieved by adding burst time of all processes and adding the avrival time of first process.
        for x in range(0,self.total_processes):
            self.total_time = self.total_time + self.process_list[x][2]
        self.total_time = self.total_time + self.process_list[0][1]

    def fcfs(self):
        """this function implements the FCFS algorithm with verbose mode"""
        #here we start from 0 and loop till total time needed to processes all processes
        #in each step we check if any processes has arrives or has any processes terminated.
        #Respective messages are displayed. If processes arrives while other processes is running it is added in ready queue.
        a = 0
        skip_a = 0
        b = 0
        true = 1
        time_counter = self.process_list[0][1]
        for x in range(0,self.total_time+1):            #loop from 0 to total time
            if skip_a == 0:                             #to check if all processes have arrived
                if x == self.process_list[a][1]:        #this condition checks if at time x any process has arrived or not and if has then places it in ready list and prints the message
                    print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    if a == 0:                          #checks if it is first process or not. if first process the move it to running list and print message.
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready -> Running.")
                    #below condition is to check if any other process arrived at same time or not
                    #if yes the process is added to ready list and message is printed
                    while a < self.total_processes-1 and self.process_list[a][1] == self.process_list[a+1][1]:
                        a += 1
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    a += 1
                    if a == self.total_processes :      #check if last process is processed. if yes then make flag so it stops checking for process arrival
                        skip_a = 1
            if b < self.total_processes:                #checks if any process is running or not if all processes have finished then skip
                if x == self.process_list[b][2] + time_counter: #checks if the process has finished execution for the time it was supposed to
                    # if yes the prints termination message and selects next process from ready list
                    time_counter = self.process_list[b][2] + time_counter
                    print("\nAt time ",x," Process ",self.process_list[b][0]," Running -> Terminated.")
                    b = b + 1
                    true = 0
                if true == 0 and b < self.total_processes:  # checks if no process is running and all processes have not finished select next process and print message
                    print("\nAt time ",x," Process ",self.process_list[b][0]," Ready -> Running.")
                    true = 1

    def fcfs_result(self):
        """this is same function as above just in this function we do not print any status message"""
        a = 0
        skip_a = 0
        b = 0
        true = 1
        time_counter = self.process_list[0][1]
        result = []
        for x in range(0,self.total_time+1):
            if skip_a == 0:
                if x == self.process_list[a][1]:
                    pass
                    #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                if a == 0:
                    #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready -> Running.")
                    a = a + 1
                if a < self.total_processes-1 and self.process_list[a][1] == self.process_list[a+1][1]:
                        a += 1
                        #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                if a == self.total_processes :
                    skip_a = 1
            if b < self.total_processes:
                if x == self.process_list[b][2] + time_counter:
                    time_counter = self.process_list[b][2] + time_counter
                    result.append([self.process_list[b][0],x])
                    #print("\nAt time ",x," Process ",self.process_list[b][0]," Running -> Terminated.")
                    b = b + 1
                    true = 0
                if true == 0 and b< self.total_processes:
                    #print("\nAt time ",x," Process ",self.process_list[b][0]," Ready -> Running.")
                    true = 1
        for y in range(0,self.total_processes):
            print(result[y][0]," ",result[y][1])

    def sjf(self):
        """this function implements SJRT algorithm"""
        #here we start from 0 and loop till total time needed to processes all processes
        #in each step we check if any processes has arrives or has any processes terminated.
        #Respective messages are displayed.
        # If processes arrives while other processes is running it checks the run time and compares with the one that is running
        # if the time for new process is less then it is executed and the one that is running is placed in ready list.
        # the ready list sorts the list if any new processes is added so every time a process terminates the process with least time left
        # is executed first.
        a = 0
        skip_a = 0
        b = 0
        true = 1
        running = []
        ready_list = []
        for x in range(0,self.total_time+1):
            if skip_a == 0:
                if x == self.process_list[a][1]:
                    print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    ready_list.append(self.process_list[a])
                    ready_list.sort(key=lambda x: x[2])             #this step sorts the ready list by the least run time first approach
                    if a == 0:
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready -> Running.")
                        running = self.process_list[a]
                    a += 1
                    if a < self.total_processes-1 and self.process_list[a][1] == self.process_list[a+1][1]:
                        a += 1
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    if a == self.total_processes :
                        skip_a = 1
            if b < self.total_processes:
                if a>0 and running != ready_list[b] and ready_list[b][2] !=0:
                    print("\nAt time ",x," Process ",running[0]," Running -> Ready.")
                    print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
                    running = ready_list[b]
                if a>0:
                    if ready_list[b][2] == 0:
                        print("\nAt time ",x," Process ",ready_list[b][0]," Running -> Terminated.")
                        b += 1
                        true = 0
                    if x < self.total_time+1 and b < self.total_processes:
                        #print(ready_list)
                        ready_list[b][2] -= 1
                        #print("\t\t",ready_list[b])
                if true == 0 and b< self.total_processes:
                    print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
                    running = ready_list[b]
                    true = 1

    def sjf_result(self):
        """this is same function as above just in this function we do not print any status message"""
        a = 0
        skip_a = 0
        b = 0
        true = 1
        running = []
        ready_list = []
        result = []
        #time_counter = self.process_list[0][1]
        for x in range(0,self.total_time+1):
            if skip_a == 0:
                if x == self.process_list[a][1]:
                    #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    ready_list.append(self.process_list[a])
                    ready_list.sort(key=lambda x: x[2])
                    if a == 0:
                        #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready -> Running.")
                        running = self.process_list[a]
                    a += 1
                    if a < self.total_processes-1 and self.process_list[a][1] == self.process_list[a+1][1]:
                        a += 1
                        #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    if a == self.total_processes :
                        skip_a = 1
            if b < self.total_processes:
                if a>0 and running != ready_list[b] and ready_list[b][2] !=0:
                    #print("\nAt time ",x," Process ",running[0]," Running -> Ready.")
                    #print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
                    running = ready_list[b]
                if a>0:
                    if ready_list[b][2] == 0:
                        result.append([ready_list[b][0],x])
                        result.sort(key=lambda x: x[0])
                        #print("\nAt time ",x," Process ",ready_list[b][0]," Running -> Terminated.")
                        b += 1
                        true = 0
                    if x < self.total_time+1 and b < self.total_processes:
                        #print(ready_list)
                        ready_list[b][2] -= 1
                        #print("\t\t",ready_list[b])
                if true == 0 and b< self.total_processes:
                    #print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
                    running = ready_list[b]
                    true = 1
        for y in range(0,self.total_processes):
            print(result[y][0]," ",result[y][1])

    def roundrobin(self):
        """this function is the implementation of Round Robin algorithm"""
        #here the implementaton uses different list to do the the swithc from one process to another
        #to switch we use a pointer to point which process is executed next. once all processes are executed and still there are
        #processes in ready list the pointer starts from first again.

        ready_list = []                 #ready list stores the process i.e works like queue
        a = 0                          #pointer to point next process to arrive
        b = 0                       #pointer to point next process in ready list
        skip_a = 0
        key = self.time_slice           #time slice value that is used to allocate specific time after which the processes switches to another process.
        sum = 0
        count = 0                   #counter to count number of cycles executed by the process
        list_item = 0
        for x in range(0,self.total_time+1):
            if skip_a == 0:
                if x == self.process_list[a][1]:
                    print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    ready_list.append(self.process_list[a])
                    list_item += 1
                    if a == 0:
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready -> Running.")
                        running = self.process_list[a]
                    a += 1
                    if a < self.total_processes-1 and self.process_list[a][1] == self.process_list[a+1][1]:
                        a += 1
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    if a == self.total_processes :
                        skip_a = 1
            if len(ready_list) > 0:     #this checks if there is more than one value in ready list.
                if count >= key:    #counter to check if time period is over or not if over switch by moving current process to ready list
                    print("\nAt time ",x," Process ",ready_list[b][0]," Running-> Ready.")
                    count = 0
                    b += 1          #pointer to point the next process in the ready list.
                    if b == list_item:
                        b = 0
                    print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
                ready_list[b][2] -= 1           #reduces the time every cycle of operation. for every cycle, the time of the process is reduced by unit
                count += 1
                if ready_list[b][2] == 0:
                    #once process terminates the counter is set to 0 and the process is removed from the ready list
                    print("\nAt time ",x," Process ",ready_list[b][0]," Running -> Terminated.")
                    del ready_list[b]
                    count = 0
                    list_item -= 1
                    b += 1
                    if b >= list_item:
                        b = 0
                    if len(ready_list) >0:
                        print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")

    def rr_result(self):
        """this is same function as above just in this function we do not print any status message"""
        ready_list = []
        a = 0
        b = 0
        skip_a = 0
        key = 8
        sum = 0
        count = 0
        list_item = 0
        result = []
        for x in range(0,self.total_time+1):
            if skip_a == 0:
                if x == self.process_list[a][1]:
                    #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    ready_list.append(self.process_list[a])
                    list_item += 1
                    if a == 0:
                        #print("\nAt time ",x," Process ",self.process_list[a][0]," Ready -> Running.")
                        running = self.process_list[a]
                    a += 1
                    if a < self.total_processes-1 and self.process_list[a][1] == self.process_list[a+1][1]:
                        a += 1
                        print("\nAt time ",x," Process ",self.process_list[a][0]," Ready.")
                    if a == self.total_processes :
                        skip_a = 1
            if len(ready_list) > 0:
                if count >= key:
                    #print("\nAt time ",x," Process ",ready_list[b][0]," Running-> Ready.")
                    count = 0
                    b += 1
                    if b == list_item:
                        b = 0
                    #print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
                ready_list[b][2] -= 1
                count += 1
                if ready_list[b][2] == 0:
                    result.append([ready_list[b][0], x])        #this part stores the result and is displayed after all processs terminated
                    result.sort(key=lambda x: x[0])
                    #print("\nAt time ",x," Process ",ready_list[b][0]," Running -> Terminated.")
                    del ready_list[b]
                    count = 0
                    list_item -= 1
                    b += 1
                    if b >= list_item:
                        b = 0
                    if len(ready_list) >0:
                        pass
                        #print("\nAt time ",x," Process ",ready_list[b][0]," Ready -> Running.")
        for y in range(0,self.total_processes):
            print(result[y][0]," ",result[y][1])


str = input("Enter the command:")
obj = jobscheduling()
if str == "-f -v -r":           #fcfs with verbose mode and random generation of processes
    num = int(input("Enter max number of processes ( greater than 3 and less than 15 "))
    obj.rand_generate(num)
    obj.fcfs()
elif str == "-f -r":            #fcfs with  random generation of processes
    num = int(input("Enter max number of processes ( greater than 3 and less than 15 "))
    obj.rand_generate(num)
    obj.fcfs_result()
elif str == "-f -processes.txt -v":         #fcfs with verbose mode and reading from file
    obj.fcfs()
elif str == "-f -processes.txt":            #fcfs with reading from file
    obj.fcfs_result()
elif str == "-sjf -v -r":       #sjrf with verbose mode and random generation of processes
    num = int(input("Enter max number of processes ( greater than 3 and less than 15 "))
    obj.rand_generate(num)
    obj.sjf()
elif str == "-sjf -r":          #sjrf with  random generation of processes
    num = int(input("Enter max number of processes ( greater than 3 and less than 15 "))
    obj.rand_generate(num)
    obj.sjf_result()
elif str == "-sjf -processes.txt -v":   #sjrf with verbose mode and reading from file
    obj.sjf()
elif str == "-sjf -processes.txt":      #sjrf with reading from file
    obj.sjf_result()
elif str == "-rr -v -r":            #round robin with verbose mode and random generation of processes
    num = int(input("Eter max number of processes ( greater than 3 and less than 15 "))
    obj.rand_generate(num)
    obj.roundrobin()
elif str == "-rr -v -r -t":         #round robin with verbose mode and random generation of processes and users time slice
    num = int(input("Eter max number of processes ( greater than 3 and less than 15 "))
    key = int(input("enter time slice(less than 10)"))
    obj.rand_generate(num)
    obj.roundrobin()
elif str == "-rr -r":           #round robin with random generation of processes
    num = int(input("Enter max number of processes ( greater than 3 and less than 15 "))
    obj.rand_generate(num)
    obj.rr_result()
elif str == "-rr -r -t":        #round robin with random generation of processes and users time slice
    num = int(input("Eter max number of processes ( greater than 3 and less than 15 "))
    key = int(input("enter time slice(less than 10)"))
    obj.rand_generate(num)
    obj.time_slice = key
    obj.rr_result()
elif str == "-rr -processes.txt -v":     #round robin with verbose mode and reading process from file
    obj.roundrobin()
elif str == "-rr -processes.txt -v -t": #round robin with verbose mode and reading process from file and users time slice
    key = int(input("enter time slice(less than 10)"))
    obj.time_slice = key
    obj.roundrobin()
elif str == "-rr -processes.txt":       #round robin with reading process from file
    obj.rr_result()
elif str == "-rr -processes.txt -t":    #round robin with reading process from file and users time slice
    key = int(input("enter time slice(less than 10)"))
    obj.time_slice = key
    obj.rr_result()