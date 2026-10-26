

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

readings = []
total = 0
valid = True

for day in days:
    consumption = float(input("Enter electricity consumption for " + day + " (kWh): "))

    if consumption < 0:
        print("Invalid electricity reading")
        valid = False
        break

    readings.append(consumption)
    total += consumption

if valid:
    average = total / 7
    highest = max(readings)
    highest_day = days[readings.index(highest)]

    print("Daily electricity readings:", readings)
    print("Total weekly consumption:", round(total, 2), "kWh")
    print("Average daily consumption:", round(average, 2), "kWh")
    print("Day with highest consumption:", highest_day)
    print("Highest consumption:", highest, "kWh")