# School managment system where teachers can add name, remove name, and change name

roasterList = ['Nitish', 'Anabel', 'Daniel', 'Onahi', 'Tobi']

while True:
    teachersChoice = input('Which operation would you like to do [Q/A/R/C/P] ')

    if (teachersChoice == 'Q'):
        break

    elif (teachersChoice == 'A'):
        newList = input(
            "What is the name of the new student you want's to add? ")
        roasterList.append(newList)

    elif (teachersChoice == 'P'):
        print(roasterList)

    elif (teachersChoice == 'R'):
        delList = int(
            input('What is the index of the student you wants to delet? '))
        del roasterList[delList]

    elif (teachersChoice == 'C'):
        delList = int(
            input('What is the index of the student you wants to delet? '))
        newList = input(
            "What is the name of the new student you want's to add? ")
        roasterList[delList] = newList

    else:
        break

print('You have succesfully exit the class managment system')
