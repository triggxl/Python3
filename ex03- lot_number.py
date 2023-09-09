#Create a program to print out sections of a lot number: "037-00901-00027"
# Country Code - Product Number - Batch Number

#my attempt
#ask for lot number
#lotNumber = input("Exercise #2: Please provide a lot number- 3 digit country code, 5 digit product code, and 5 digit batch number")
#print("Country code:" + lotNumber[0:2], "Product code:" + lotNumber[3:8], "Batch number:" + lotNumber[-5:])


#Solution:
lot_number = "037-00901-00027"

print("Country code:", lot_number[0:3]) #start included, end is not
print("Product code:", lot_number[4:9])
print("Batch number:", lot_number[10:])
