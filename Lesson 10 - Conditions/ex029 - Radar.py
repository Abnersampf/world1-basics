speed = float(int(input("What is the car's current speed? ")))
if speed > 80:
    speeding_ticket = (speed - 80) * 7
    print("FINED! You exceeded the speed limit of 80km/h!")
    print(f"You have to pay a fine of R${speeding_ticket}!")
print("Have a good day! Drive safely!")