

capacity = 50
passengers = 0
total_boarded = 0
total_exited = 0

number_of_stops = int(input("Enter number of bus stops: "))

for stop in range(1, number_of_stops + 1):
    print("\nBus Stop", stop)

    exiting = int(input("Enter passengers getting off: "))

    if exiting < 0 or exiting > passengers:
        print("Invalid number of exiting passengers")
        continue

    passengers -= exiting
    total_exited += exiting

    boarding = int(input("Enter passengers boarding: "))

    if boarding < 0 or passengers + boarding > capacity:
        print("Invalid boarding count or bus capacity exceeded")
        continue

    passengers += boarding
    total_boarded += boarding

    print("Passengers onboard:", passengers)

print("\nJourney Summary")
print("Total passengers boarded:", total_boarded)
print("Total passengers exited:", total_exited)
print("Final occupancy:", passengers)
print("Available seats:", capacity - passengers)
