
#Paul Rosales
#6/7/23
#this program runs through a txt file of data and gives the number of readings, the lowest and highest readings,
#and the average of all of them. It displays this information in a seprate file 


#Test Cases
#pollutant 1
#blanco pollutant 2
#pollutant 3
#pollutant 4
# enter nothing for all
# enter wrong info
#enter outside 1-4
#enter outside 1-12

def main():
    #This takes in info from user and makes sure it is acceptable
    river = input('Data for River: ')
    while river == '':
        river = input('Data for River: ')
    
    month = int(input('Data for month: '))
    while month == '' or (month < 1 or month > 12) :
        month = int(input('Data for month: '))

    
    print('\n' + '\n' + 'Available pollutants:' + '\n' + '1. Arsenic' + '\n' + '2. Lead')
    print('3. Fertilizer' + '\n' + '4. Pesticides')
    pollutant = int(input('Which pollutant? '))

    while pollutant == '' or (pollutant < 1 or pollutant > 4):
        print('\n' + '\n' + 'Available pollutants:' + '\n' + '1. Arsenic' + '\n' + '2. Lead')
        print('3. Fertilizer' + '\n' + '4. Pesticides')
        pollutant = int(input('Which pollutant? '))
        
    #This opens the files and preparese them for what they will be doing
    pollutionSummary = open('PollutionSummary.txt', 'w')
    riverStats = open('RiverPollutionData.txt', 'r')

    #This provides variables to be used in the while loop
    readingsCount = 0
    total = 0
    low = 99
    high = 0
    material = 'Pesticides'
    pollutionSumLine = riverStats.readline()

    #This loops each line of code from the pollution data txt
    while pollutionSumLine != '':
        #more variables to be changed 
        compareHigh = 0
        compareLow = 99

        #This reads the lines splits them and creates and edits variables to be calculated
        pollutionSumLine = riverStats.readline()
        flieStringSplit = pollutionSumLine.split('\t')
        if river == flieStringSplit[0] and str(month) == flieStringSplit[1]:
            readingsCount += 1
            if pollutant == 1:
                total += float(flieStringSplit[3])
                compareHigh = float(flieStringSplit[3])
                compareLow = float(flieStringSplit[3])
                material = 'Arsenic'
                
            elif pollutant == 2:
                total += float(flieStringSplit[4])
                compareHigh = float(flieStringSplit[4])
                compareLow = float(flieStringSplit[4])
                material = 'Lead'
                
            elif pollutant == 3:
                total += float(flieStringSplit[5])
                compareHigh = float(flieStringSplit[5])
                compareLow = float(flieStringSplit[5])
                material = 'Fertilizer'
            else:
                total += float(flieStringSplit[6])
                compareHigh = float(flieStringSplit[6])
                compareLow = float(flieStringSplit[6])
        #this calculates the lowest and highest readings and below that gives the average
        if compareHigh > high:
            high = compareHigh
        if low > compareLow:
            low = compareLow
    avg = round(total / readingsCount, 3)

    #This writes data in the other file called pollution summary

    pollutionSummary.write('Data for River: ' + river + '\n')
    pollutionSummary.write('Data for Month: ' + str(month) + '\n')
    pollutionSummary.write('Data for Pollution: ' + material + '\n' + '\n')
    pollutionSummary.write('Number of readings  ' + str(readingsCount) + '\n')
    pollutionSummary.write('Average of readings   ' + str(avg) + '\n')
    pollutionSummary.write('Lowest reading        ' + str(low) + '\n')
    pollutionSummary.write('Highest reading       ' + str(high) + '\n')
    
    #This closes all the files used 
    pollutionSummary.close()
    riverStats.close()


#1. I tried apporach it a bit at a time like I did in my last project where I test frequently after typing a bit of
    #code. I got stuck in the beginign where I was not sure how to write and manitpulate the data into the file requested
    #I went to tutoring for help where my tutor helped me understand what was supposed to happen and reviewing previous concepts while making
    #sure I was understanding. I was then able to move forward and complete the assingment with minimal sturggle
#2. I tried using numbers that would break my program and with each break I fixed the code then at the end review all the test cases
    #I think that my code may have some errors I oversaw or test cases I didnt think of so I would like to improve on those
#3. I learned more about coding to transfer data from file to fila and gained a better understanding of how files work
    #and how to work with them. Next project I am going to review the materail requried for it first so that I can come in to the
    #project with a much more refreshed understanding of the material

main()
