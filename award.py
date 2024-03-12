# This project asks the user to input the 3 times they recieved in the Triathlon. These minutes are added up and stored.
swimming = int(input("Swimming-time in minutes: "))
cycling = int(input("cycling-time in minutes: "))
running = int(input("running-time in minutes: "))
Triathlon = swimming + cycling + running
print(f"Total time: {Triathlon} minutes")
# Depending on the total time, the user will receive one of three awards or none.
# If the triathlon variable is less than 100, it will print "Provincial Colours", between 101 and 105 will print "Provincial Half Colours" and 106 to 110 prints "Provincial Scroll"
if Triathlon <= 100:
    print("Provincial Colours")
elif Triathlon >= 101 and Triathlon <= 105:
    print("Provincial Half Colours")
elif Triathlon >= 106 and Triathlon <= 110:
    print("Provincial Scroll")
else:
    print("No award")

