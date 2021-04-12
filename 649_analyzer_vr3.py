### PROGRAMMER'S BLOCK ###

# Name: Shaheen Eshghi
# CMPT 120
# Instructor: Diana Cukierman
# FINAL Assignment - 649

###INTRO#####################################################################
import os

from math import floor

lread = []  # used to list all available data from "read csv" fucntion
lcurrent = []  # used to modify lread based on user data selection
lres = [0] * 5  # list of tally of numbers based on range occurences
lress = [0] * 5
lout = []  # list of output printed to file

ldate = []  # list of dates of draws depending on user selection
ldraws = []  # list of drawn numbers depending on user selection
lbonus = []  # list of bonus numbers depending on user selection
lprize = []  # list of prizes depending on user selection
lwinners = []  # list of numbers of winners depending on user selection
lavgwon = []  # list of average winnings per winner depending on user selection
lmonths = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
           "Dec"]  # list of months used to correspond by index during user selection later on

print("Welcome to the CMPT 120 6-49 Processing system!".center(70))
print("=======" * 10)

print("You first need to provide the input file name\nYou will be asked to provide the output file name later\n")

print("The input file should be in this  folder\nThe output file will be created in this folder\n")

print(
    "You will be able to provide new names for the files\nOr accept the default names. Both files should have the extension  .csv\n")

uIname = input("Type x for INPUT file name 'IN_data_draws3.csv', or a new file name ==> ")

if uIname.lower() != "x":  # Validates user entry to adjust file name accordingly
    os.rename("IN_data_draws3.csv", uIname)
else:
    uIname = "IN_data_draws3.csv"


###DATA PROCESSING#############################################################


###trace print
##print()
##print (lread)
##print()
###


def read_csv_into_list_of_lists(IN_file):
    '''
    PROVIDED. CMPT 120
    A csv file should be available in the folder (where this program is)
    A string with the name of the file should be passed as argument to this function
    when invoking it
    (the string would include the csv extension, e.g "ID_data.csv")
    '''

    import csv

    lall = []

    print("\n.... TRACE - data read from the file\n")
    with open(IN_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for inrow in csv_reader:
            print(".......", inrow)
            lall.append(inrow)

    return lall


lread = read_csv_into_list_of_lists(uIname)
print()

def convert_lall_to_separate_lists(lall):
    #print("eee",lall)
    '''
      RECOMMENDED THAT YOU DEVELOP THIS FUNCTION

      input parameter: list of lists with all the data
      as returned from read_csv_into_list_of_lists(...)

      return: several lists:
          dates of draws,
          numbers drawn for each draw,
          jackpot for each draw
          number of winners for each draw

     these lists would be such that accross the lists,
     the same index refers to one draw.
    '''

    for k in range(len(lall)):  # Appends different sections of past data to applicable lists (sort them in a way)
        ldate.append(lall[k][0])
        ldraws.append(lall[k][1:8])
        lprize.append(lall[k][8])
        lwinners.append(lall[k][9])
        if lall[k][9] != "0":
            lavgwon.append(int(lall[k][8]) / int(lall[k][9]))
        else:
            lavgwon.append("0")

        ###trace print
        print(ldate)
        print(ldraws)
        print(lprize)
        #print(lwinners)
        #print("qqqq",int(lall[k][8]) / int(lall[k][9]))
        print(lavgwon)
        print()
        ###
    return lavgwon

def append_1_draw_to_output_list(date, lfreq_ran, avg_paid):
    '''
    PROVIDED. CMPT 120
    this function would append one line (the result associated to one draw)
    to a list. (this list will later be used to create the output file)


    The input parameters to this function are:
        - the list used to incorporate all the results
        - a string representing the date of this one draw to be appended
        - the list with the range frequency distribution for this draw
        - the average paid to each winner for this draw
    '''
    dcount = 0
    while dcount < len(date):
        lout.append("'" + date[dcount] + "'" + ",")
        for freq in lfreq_ran:
            lout.append(str(freq) + ",")
        lout.append(str(avg_paid) + "\n")
        dcount += 1
    return

def dateandavg(lout,date,num_range_frequency,convert):
    dcount = 0
    while dcount < len(date):
        num_range_frequency = num_range_frequency(lout)
        convert = convert_lall_to_separate_lists(lout)
        lout.append("'" + date[dcount] + "'" + "," +str(num_range_frequency)+", "+str(convert)+"\n" )
    return



def write_list_of_output_lines_to_file(lout, file_name):
    '''
    PROVIDED. CMPT 120
    Assumptions:
    1) lout is the list containing all the lines to be saved in the output file
    2) file_name is the parameter receiving a string with the exact name of the output file
       (with the csv extension, e.g "OUT_results.csv")
    3) after executing this function the output file will be in the same
       directory (folder) as this program
    4) the output file contains just text representing one draw data per line
    5) after each line in the file  there is the character "\n"
       so that the next draw is in the next line, and also
       there is (one single) "\n" character after the last line
    6) after the output file was created you should be able to open it
       with Excell as well
    '''
    #print(convert_lall_to_separate_lists())
    fileRef = open(file_name, "w")  # opening file to be written
    convert = convert_lall_to_separate_lists(lout)
    count = 0
   # print('bbbbbbbbbbbb', lout)
    num_range = num_range_frequency(lout)
   # print(num_range,"iiii")
    #append_curr = append_1_draw_to_output_list(ldate,num_range_frequency(lout),convert_lall_to_separate_lists(lout))
    for line in lout:
        #avgwon_curr = avgwon.append(lout[len(lout)][8] / lout[len(lout)][9])
        #fileRef.write(', '.join(line) + avgwon_curr + '\n')
        #print("wwww",str((int(line[len(line)][8]) / int(line[len(line)][9]))))
        #fileRef.write(', '.join(line) + ', ' + str(convert[count]) + '\n')
        #num_range = num_range_frequency(lout)
        fileRef.write(line[0] + ', ' + str(num_range[count])+ ", "+str(convert[count]) + '\n')
        #fileRef.write( str(append_curr[count])+ ", "+str(convert[count]) + '\n')
        #print("nnnnn",line)
        #print("iiiii",fileRef.write(convert_lall_to_separate_lists(line)))
        count+=1
    fileRef.close()
    return



###STATS###################################################################

def num_Draws(lall):  # Return the numbers of draws processed based on user selection
    return str(len(lall))


def max_Jackpot(lall):  # Finds max jackpot and its date depending on data selected by user
    mJack = 0  # Biggest total Jackpot
    imaxdate = 0  # Index of date of above
    for k in range(len(lall)):
        if int(lall[k][8]) > int(mJack):
            mJack = lall[k][8]
            imaxdate = lall[k][0]
    return "Max Jackpot: $" + str(mJack), "Date of Max Jackpot:", imaxdate


def num_tally_range(lall):  # Provides a tally of the occurence of each number from 0-49 based on user data selection
    global lnumtally
    lnumtally = [0] * 50  # Number of times each number is drawn
    for k in range(len(lall)):
        # Keep track of numbers won and tally to a list
        for i in range(1, 8):
            lnumtally[int(lall[k][i])] += 1
        # Check range of numbers won

    print("Number of times each numbers was drawn:\n" + str(lnumtally))


def per_Jackpot(lall):  # Finds the maximum winnings per winner and date it occured based on user selected data
    perJack = 0  # Biggest amount won per person per jackpot
    iperdate = 0  # Date of above
    for k in range(len(lall)):
        # Check number of winners and compare winnings per person with previous maximum and record date
        if int(lall[k][9]) > 0 and int(lall[k][8]) / int(lall[k][9]) > perJack:
            perJack = int(lall[k][8]) / int(lall[k][9])
            iperdate = lall[k][0]
    return "MAX Average Winnings: $" + str(perJack), "Date of MAX Average Won: " + str(iperdate)


def num_range_frequency(
        lall):  # Finds the frequency of numbers based on the ranges they occur (0,10], (10,20], (20,30], (30,40], (40,50)
    lres = [[],[],[],[],[]]
    for i in range(len(lall)):
        lres[i] = []
        k = [0,0,0,0,0]
        lstOnlyDN = []
        for x in range(1, 8):
            lstOnlyDN.append(int(lall[i][x]))
        for num in lstOnlyDN:
            #print(floor(int(num) / 10), 'kkkkkkkkkkkkkkkkkkk')
            k[floor(int(num) / 10)] += 1
        lres[i] = k
##    print('aaaaaaaaaaaaaaaaaaaaa', len(lres))
    return lres


def most_freq_num(
        ldrawn):  # returns a list with the 6 most frequently drawn numbers based on user selection of data to be processed
    lfreq = []
    goal = ""
    print("Six most frequently drawn numbers:")
    for k in range(6):
        goal = max(ldrawn)
        lfreq.append(ldrawn.index(goal))
        print("number " + str(lfreq[k]) + " was drawn " + str(goal) + " time(s)")
        ldrawn.remove(goal)

def num_range_frequency_2(lall): #Finds the frequency of numbers based on the ranges they occur (0,10], (10,20], (20,30], (30,40], (40,50)
    for i in range(len(lall)):
        lstOnlyDN = []
        for x in range(1, 8):
            lstOnlyDN.append(int(lall[i][x]))
        for num in lstOnlyDN:
            k = 0
            while (num > k * 10):
                k = k + 1
            lress[(k - 1)] += 1
    return lress


def draw_graph(): #Graphs the data from the num_tally_range function, scales data by multiplying range tally by 50
    import turtle as t
    t.penup()
    t.setposition(-200,-200)
    t.fillcolor("magenta")
    for k in range(len(lress)):
        t.begin_fill()
        t.pendown()
        t.forward(50)
        t.left(90)
        t.forward(lress[k]*50)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(lress[k]*50)
        t.left(90)
        t.forward(100)
        t.end_fill()


###MAIN########################################################################

print(
    "Please choose one of three options:\nType ALL to process all the data\nType SEL to process selected draws\nType END to end this program")

uData = input("Type ALL, SEL or END (not case sensitive) ==> ")

while uData.upper() != ("ALL") and uData.upper() != ("SEL") and uData.upper() != (
"END"):  # Validates user's response and prompts again if invalid
    print("That is not a valid answer. Try again!")
    uData = input("Type ALL, SEL or END (not case sensitive) ==> ")

if uData.upper() == "ALL":
    print("============= ALL the data will be processed ============")
    lcurrent = lread

elif uData.upper() == "SEL":
    uData = input("Please select desired month (1 thru 12) ==> ")
    while not uData.isdigit() or int(uData) > 12 or int(
            uData) < 1:  # Validates user's response and prompts again if invalid
        print("That is not a valid answer. Try again!")
        uData = input("Please select desired month (1 thru 12) ==> ")
    print("============= SELECTED data will be processed ============")
    count = 0

    while count < len(
            lread):  # Verifies which input lists from lread contain user selected months and adds those specific lists to a new list
        # print('jjjjjjjjj', lread[i])
        # count = len(lread)
        # for i in range(count):
        #   print(i)
        MData = lread[count][0]
        if (MData[2:5] == lmonths[int(uData)] or MData[3:6] == lmonths[
            int(uData)]):  # Checks the month portion of data and compares against user selected filter
            # if months[int(uData)] != lread[count][3:6]:
            # lread.remove(lread[i])
            # current_list.append(lread[i])
            lcurrent.append(lread[count])
        count += 1


elif uData.upper() == "END":
    print("BYE....no more stats for you!!")
    exit()

##count = len(lread)
##for i in range(count):
##    CData = lread[i][0]
##    print(CData)

print(
    "\nPlease confirm the output file name for your selected data\nIf there is a file with this name in the folder it will be overwritten")

uOname = input("Type x for OUTPUT file name 'OUT_results3.csv', or a new file name ==> ")

if uOname.lower() != "x":
    os.rename("OUT_results3.csv", uOname)
else:
    uOname = "OUT_results3.csv"
# print('bbbbbbb', current_list)

print()
print("JUST TO TRACE, the draw(s) being processed is:\n", lcurrent)
print()
print("TRACING: Here is the output saved to the file!\n", lout)
print()

print("=======" * 2 + "STATS" + "=======" * 2)
print()
print("Draws Processed: " + num_Draws(lcurrent))
print()
print(max_Jackpot(lcurrent))
print()
print(num_tally_range(lcurrent))
print()
print(per_Jackpot(lcurrent))
print()
print(
    "Number of numbers in each range - all selected draws considered \n ranges: (0,10], (10,20], (20,30], (30,40], (40,50)",
    num_range_frequency(lcurrent))
print(
    "Number of numbers in each range - all selected draws considered \n ranges: (0,10], (10,20], (20,30], (30,40], (40,50)",
    num_range_frequency_2(lcurrent))
print()
print(most_freq_num(lnumtally))
print()
print()

uGprompt = input("Would you like to graph the ranges distribution? (Y/N) ==> ")
while uGprompt.upper() != "Y" and uGprompt.upper() != "N":
    print("That is not a valid answer. Try again!")
    uGprompt = input("Would you like to graph the ranges distribution? (Y/N) ==> ")

if uGprompt.upper() == "Y":
    print("=======" * 2 + "GRAPHING..." + "=======" * 2)
    draw_graph()
else:
    print("NO graph for you! BYEEE :)")
    print()
    pass

#convert_lall_to_separate_lists(lcurrent)

append_1_draw_to_output_list(ldate, num_range_frequency(lcurrent), lavgwon)
#print("www",lcurrent)
#print("ttt",num_range_frequency(lcurrent))
#print("eee",convert_lall_to_separate_lists(lcurrent))
write_list_of_output_lines_to_file(lcurrent,uOname)
#print("mmmm",dateandavg(lcurrent,ldate,num_range_frequency(lcurrent),convert_lall_to_separate_lists(lcurrent)))

print("END OF PROGRAM. HAVE A NICE DAY!")

