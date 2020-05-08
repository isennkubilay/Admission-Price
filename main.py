baby_price = 0.00
child_price = 14.00
adult_price = 23.00
senior_price = 18.00

baby_limit = 2 
child_limit = 12 
adult_limit = 64 

total = 0

line = input("Enter the age the guest (blank to finish): ")

while line != "":
  age = int(line)

  if age <= baby_limit:
    total = total + baby_price
  elif age <= child_limit:
    total = total + child_price
  elif age <= adult_limit:
    total = total + adult_price
  else:
    total = total + senior_price

  line = input("Enter the age of the guest (blank to finish): ")
  print(f"The total for that group is {total:.2f}")