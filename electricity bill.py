units = int(input("Please enter Number of Units you Consumed : "))
if(units < 50):
    amount = units * 2.60
    supercharge = 25
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    supercharge = 35 
elif(units <= 200):
    amount = 130 + 162.50 + 526 ((units - 200) * 8.45)
    supercharge = 75
total = amount + supercharge 
print("\nElectricity Bill = %.2f"  %total)
