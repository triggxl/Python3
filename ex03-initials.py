#Data types: string = sequence of characters
# invoice number, zip code
# len -1 gives last character
# splicing myString[start:finish] can omit or leave off like this myString[-2:] grabs last two

#Create a program that asks for the users full name and then returns their intials

#firstName = input("What is your first name?")
#middleName = input("What is your middle name?")
#lastName = input("What is your last name?")

#print("Your initials are: ", firstName[0], middleName[0], lastName[0])

#Create a program to print out sections of a lot number: "037-00901-00027"
# Country Code - Product Number - Batch Number

#ask for lot number

lotNumber = input("Exercise #2: Please provide a lot number- 3 digit country code, 5 digit product code, and 5 digit batch number")


print("Country code:" + lotNumber[0:2], "Product code:" + lotNumber[3:8], "Batch number:" + lotNumber[-5:])
