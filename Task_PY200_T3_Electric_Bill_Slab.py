units = int(input("Enter electricity units: "))

bill = 0

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

elif units <= 500:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

else:
    bill = (100 * 2) + (100 * 3) + (300 * 5) + (units - 500) * 8

# Add fixed charge
bill = bill + 50

print("Total Electricity Bill:", bill)