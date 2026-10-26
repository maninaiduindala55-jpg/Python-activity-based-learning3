n = int(input("Enter number of routes: "))

if n <= 0:
    print("Invalid number of routes")

else:
    fuel_price = float(input("Enter fuel price per litre: "))

    if fuel_price <= 0:
        print("Invalid fuel price")

    else:
        lowest_cost = None
        best_route = ""

        for i in range(n):
            route_name = input("Enter route name: ")
            distance = float(input("Enter distance in km: "))
            mileage = float(input("Enter mileage in km/litre: "))

            if distance <= 0 or mileage <= 0:
                print("Invalid route details")

            else:
                fuel_required = distance / mileage
                fuel_cost = fuel_required * fuel_price

                print("Route:", route_name)
                print("Fuel required:", round(fuel_required, 2), "litres")
                print("Fuel cost: Rs.", round(fuel_cost, 2))

                if lowest_cost is None or fuel_cost < lowest_cost:
                    lowest_cost = fuel_cost
                    best_route = route_name

        if best_route != "":
            print("Lowest-cost route:", best_route)
            print("Lowest fuel cost: Rs.", round(lowest_cost, 2))