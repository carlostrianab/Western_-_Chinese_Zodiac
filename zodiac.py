## STUDENT: CARLOS ALBERTO TRIANA BRIGANTE - ID: 21503286

#THIS PROGRAM TAKES USER ID, DATE OF BIRTH AND NAME TO MAKE A TABLE SORTED BY USER ORDER 
#AND DISPLAY INFORMATION ABOUT THE AGE AND ZODIAC SIGN.

#COURSEWORK 3

#We import module date, HTML and display that will help us calculating age and displaying
#the table with the data 

#We import the 're' module that will help to make regex operations to filter information 
#from .txt files 

from datetime import date
from IPython.display import HTML, display
import re



def age(year):
    """Receives the year of birth(integer) as input and return the age"""
    #currentYear is calculated with the date.today method from the 'date' module
    #which calculates the current year
    currentYear = (date.today().year)
    if(year>currentYear):
        return "You haven´t been born yet!"
    born = currentYear - year
    return born


def westernZodiac(day,month):
    
    """ Receives the day(integer) and month(integer) of birth of a given user and return it's
    western zodiac sign"""
    
    #Given the day and month the conditionals will search through the range
    #of dates, and calculate the zodiac sign depending on the input
    if(month == 12 and day>=22 or month == 1 and day <= 19):
        sign = 'Capricorn'
    elif(month == 1 and day >= 20 or month == 2 and day <= 18):
        sign = 'Aquarius'
    elif(month == 2 and day >= 19 or month == 3 and day <= 20):
        sign = 'Pisces'
    elif(month == 3 and day >= 21 or month == 4 and day <= 19):
        sign = 'Aries'
    elif(month == 4 and day >= 20 or month == 5 and day <= 20):
        sign = 'Taurus'
    elif(month == 5 and day >= 21 or month == 6 and day <= 21):
        sign = 'Gemini'
    elif(month == 6 and day >= 22 or month == 7 and day <= 22):
        sign = 'Cancer'
    elif(month == 7 and day >= 23 or month == 8 and day <= 22):
        sign = 'Leo'
    elif(month == 8 and day >= 23 or month == 9 and day <= 22):
        sign = 'Virgo'
    elif(month == 9 and day >= 23 or month == 10 and day <= 22):
        sign = 'Libra'
    elif(month == 10 and day >= 23 or month == 11 and day <= 22):
        sign = 'Scorpio'
    else:
        sign = 'Sagittarius'
  
    return sign

 
def displayTable(data):
    
    """ Given a data array that includes [UID, NAME, DOB, AGE, WESTERN ZODIAC, CHINESE ZODIAC], the program will reder 
    that information and show it in a table in HTML format"""
    
    #'display' and 'HTML' functions from the display module are used, we loop
    #through the data array and then we render a table in HTML format 
    html = "<table>"
    html += "<tr><td><h3>UID</h3></td><td><h3>Name</h3></td><td><h3>DoB</h3></td><td><h3>Age</h3></td><td><h3>Western Zodiac</h3></td><td><h3>Chinese Zodiac</h3></td></tr>"
    for row in data:
        html += "<tr>"
        for field in row:
            html += "<td><h4>%s</h4></td>"%(field)
        html += "</tr>"
    html += "</table>"
    display(HTML(html))
    


def zn_zodiac(year):
    
    """ Receives the day(integer) and month(integer) of birth of a given user and return it's
    western zodiac sign"""
    
    zn = ''
    cycle = 12
    positiveYear = abs(year)
    
    #We use modulus(%) operator to find what number in a 12 year cycle does each birth date 
    #corresponds 
    
    rat = 2020 % cycle
    ox = 2021 % cycle
    tiger = 2022 % cycle
    hare = 2023 % cycle
    dog = 2021 % cycle
    snake =2022 % cycle 
    horse = 2023 % cycle 
    sheep = 2027 % cycle
    monkey = 2028 % cycle
    rooster = 2029 % cycle
    dragon = 2030 % cycle
    pig = 2031 % cycle
    
    #we search for the years bigger that 12 in which we have to 
    #to apply the modulus operator to find in what 12 year cycle category does
    #the inputed year of birth fits.
    if(positiveYear>12):
        if(positiveYear % cycle == rat):
            zn = 'Rat'
        elif(positiveYear % cycle == ox):
            zn = 'Ox'
        elif(positiveYear % cycle == tiger):
            zn = 'Tiger'
        elif(positiveYear % cycle == hare):
            zn = 'Hare'
        elif(positiveYear % cycle == dog):
            zn = 'Dog'
        elif(positiveYear % cycle == snake):
            zn = 'Snake'
        elif(positiveYear % cycle == horse):
            zn = 'Horse'
        elif(positiveYear % cycle == sheep):
            zn = 'Sheep'
        elif(positiveYear % cycle == monkey):
            zn = 'Monkey'
        elif(positiveYear % cycle == rooster):
            zn = 'Rooster'
        elif(positiveYear % cycle == dragon):
            zn = 'Dragon'
        else:
            zn = 'Pig'
    else:
        #Here we just take the year, since no calculation is needed
        if(positiveYear == rat):
            zn = 'Rat'
        elif(positiveYear == ox):
            zn = 'Ox'
        elif(positiveYear == tiger):
            zn = 'Tiger'
        elif(positiveYear == hare):
            zn = 'Hare'
        elif(positiveYear == dog):
            zn = 'Dog'
        elif(positiveYear == snake):
            zn = 'Snake'
        elif(positiveYear == horse):
            zn = 'Horse'
        elif(year == sheep):
            zn = 'Sheep'
        elif(positiveYear == monkey):
            zn = 'Monkey'
        elif(positiveYear == rooster):
            zn = 'Rooster'
        elif(positiveYear == dragon):
            zn = 'Dragon'
        else:
            zn = 'Pig'
    
    return zn
  
        

def userInput():  
    
    """Takes the user's ID, name and DoB through different inputs and creates
    a data list with the ID, name, dob, age, western and chinese zodiac signs"""
    #fixedNumber variable will determine how many data entries you will have in the program 
    fixedNumber = 6
    counter = 0
    global data
    data = []
    finishProgram = True
    while(counter<fixedNumber and finishProgram == True):
        #This 'print()' function shows the number of entries left.
        print('You have', fixedNumber - counter, 'entries left.')
        #Input with type check for the user ID, doesn't allow types of values different to numbers
        #and the input can be only 2 digits long
        #user can type 'end' to finish the program
        askAgain = True      
        while(askAgain == True):
            user = input('Enter a 2-digit user ID or type "end" to finish: ')
            try:
                if(user == 'end'):
                    finishProgram = False
                    return finishProgram
                userId = int(user)
                if(len(str(userId)) > 2):
                    print("the value can't have more than 2 digits!")
                else:
                    askAgain = False
            except ValueError:
                print('this is not a number')     
        #Input for the name, accepts any alpha-numeric value.
        name = input("Input your name: ")           
        #Input for the day, it only accepts 31 days and also accepts numeric values only.
        askAgain = True
        while (askAgain == True):
            try:
                day = abs(int(input('Enter your day of birth: ')))
                if(day > 31):
                    print("The month has only 31 days! try again")
                else:
                    askAgain = False
            except ValueError:
                print('Please enter your day of birth in numeric value')
        #Input for the month, it only accepts 12 months and also accepts numeric values only.
        askAgain = True
        while (askAgain == True):
            try:
                month = abs(int(input('Enter your month of birth: ')))
                if(month > 12):
                    print("There are only 12 months in the year")
                else:
                    askAgain = False
            except ValueError:
                print('Please enter your month of birth in numeric value')
        #Input for the year, it only accepts numeric values only.
        askAgain = True
        while (askAgain == True):
            try:
                year = int(input('Enter your year of birth: '))
                askAgain = False
            except ValueError:
                print('Please enter your year of birth in numeric value')

        #we declare 'dob' that will generate a string with day/month/year
        dob = str(day) + '/' + str(month) + '/' + str(year)

        data.append([userId,name,dob,age(year),westernZodiac(day,month),zn_zodiac(year)])

        counter = counter + 1 
        #sorted function helps us organize the data depending on the user ID
        data = sorted(data, key=lambda x: x[0]) 
        return data

#we call 'userInput()' and 'displayTable()' so the system runs those functions     

#We use the open function to open the 'userData.txt' file written in the 'writeInfo(data)' function
def readNewData(dataFile):
    """""Takes a .txt data file with an 'UID USERNAME DOB' format and creates a data array with 
    'UID USERNAME AGE DOB WESTER-SIGN CHINESE-SIGN'"""
    
    userData = open(dataFile,'r')

    extractedData = []
    global newData
    newData = []
    
    #If the .txt file is not in the correct format the function will go to a exception
    #mode and throw an error message.
    try:
        for line in userData:
            #Cleaning and filtering the information using 'split()' method.
            line = line.split()
            extractedData.append(line)

        extractedData = extractedData[1:len(extractedData)]


        for array in extractedData:
            userID = array[0]
            name = array[1] + ' ' +  array[2]
            dob = array[3].split('-')
            year = dob[0]
            month = dob[1]
            day = dob[2]

            dobEntry = str(day) + '/' + str(month) + '/' + str(year)

            newData.append([userID,name,dobEntry,age(int(year)),
                            westernZodiac(int(day),int(month)),zn_zodiac(int(year))])

        userData.close()
        newData = sorted(newData, key=lambda x: x[0]) 
        return newData
    
    except IndexError:
        print('The .txt file is not in the correct format')
        print('please try with a .txt file with the following format:')
        print('UID NAME DOB')
        

def writeNewData(newData):
    """Takes the 'newData' created in the 'readNewData(datafile)' function and creates a new
    .txt file with 'UID NAME AGE WESTERN-ZODIAC CHINESE-ZODIAC' information"""
    
    data = open('Zodiac.txt', 'w')
    data.write('UID Name DoB Age Western-Zodiac Chinese-Zodiac\n')
    for i in newData:
        data.write(i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + str(i[3]) + ' ' + i[4] + ' ' + i[5]+'\n')
    data.close()
        
   

def main():
    dataFile = 'UserData.txt'
    readNewData(dataFile)
    displayTable(newData)
    writeNewData(newData)
    

main()
