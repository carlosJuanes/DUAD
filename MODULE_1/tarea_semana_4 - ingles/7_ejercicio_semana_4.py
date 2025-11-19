#7. Create an algorithm that asks the user for a time in seconds and calculates if it's less than, greater than, or equal to 10 minutes.

#If it's less, display how many seconds would be needed to reach 10 minutes.
#If it's greater, display "Greater".
#If it's exactly equal, display "Equal".

time_in_seconds=int(input(f"please enter your time in seconds= "))

if time_in_seconds<600:
    seconds_remaining=600-time_in_seconds
    print(f"  {seconds_remaining} second are needed to reach 10 minutes ")
elif time_in_seconds>600:
    print(f" greater")
else:
    print(f" equal")