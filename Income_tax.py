#income tax system

income=float(input("Please enter your income:"))

#making decision
if(income<=11850):
    band="Additional rate"
    rate=45

elif(income>=11850 and income<=46350):
    band="Higher rate"
    rate=40

elif(income>46351 and income >150000):
    band="basic"
    rate=20

else:
    band="Personal allowance"
    rate=0

print("Your tax band is:",band)

print("Your tax rate is:",rate)