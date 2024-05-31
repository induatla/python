# electricity bill
previous_month_reading=int(input("Enter previous month readings :"))
current_month_reading=int(input("Enter current month readings :"))
units=current_month_reading - previous_month_reading
print("number of units consumed in this month:",units)
if(units<=100):
  amt=units*1
  print(amt)
elif(units>=101 and units<=200):
  amt=units*2
  print(amt)
elif(units>=201):
  amt=units*5
  print(amt)
else:
  print("thank u")
