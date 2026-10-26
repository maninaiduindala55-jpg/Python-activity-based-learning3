vehicle = input("Enter vehicle type (car/bike): ").lower()
entry = int(input("Enter entry hour (0-23): "))
exit_time = int(input("Enter exit hour (0-23): "))

if vehicle == "car":
    rate = 30
elif vehicle == "bike":
    rate = 10
else:
    rate = 0
    print("Invalid vehicle type")

if rate > 0:
    if exit_time < entry:
        duration = (24 - entry) + exit_time
        surcharge = 20
    else:
        duration = exit_time - entry
        surcharge = 0

    hours = duration

    if duration > hours:
        hours = hours + 1

    basic_fee = hours * rate

    if basic_fee > 200:
        basic_fee = 200

    total_fee = basic_fee + surcharge

    print("Parking duration:", duration, "hours")
    print("Charged hours:", hours)
    print("Basic fee: Rs.", basic_fee)
    print("Overnight surcharge: Rs.", surcharge)
    print("Total fee: Rs.", total_fee)