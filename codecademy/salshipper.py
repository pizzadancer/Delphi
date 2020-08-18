# shipping_cost = 0
premium_ship = 125.00

# Ground Shipping
def ground_shipping(package_weight):
    if package_weight < 2:
        shipping_cost = (package_weight * 1.50) + 20
    elif 2 < package_weight <= 6:
        shipping_cost = (package_weight * 3.00) + 20
    elif 6 < package_weight <= 10:
        shipping_cost = (package_weight * 4.00) + 20
    else:  # over 10 lbs
        shipping_cost = (package_weight * 4.75) + 20

    return shipping_cost


# Drone Shipping
def drone_shipping(package_weight):
    if package_weight < 2:
        shipping_cost = package_weight * 4.50
    elif 2 < package_weight <= 6:
        shipping_cost = package_weight * 9.00
    elif 6 < package_weight <= 10:
        shipping_cost = package_weight * 12.00
    else:  # over 10 lbs
        shipping_cost = package_weight * 14.25

    return shipping_cost


# def premium_ship():
#     return 125.00


def cheapest_shipping():
    package_weight = float(input("What's the package_weight of your package?: "))
    ground_ship = ground_shipping(package_weight)
    drone_ship = drone_shipping(package_weight)
    if ground_ship < drone_ship and ground_ship < premium_ship:
        print("Ground is the low low")
        print(ground_ship)
    elif drone_ship < ground_ship and drone_ship < premium_ship:
        print("Drone is the low low")
        print(drone_ship)
    elif premium_ship < drone_ship and premium_ship < ground_ship:
        print("Premium Ground is the low low")
        print(premium_ship)


cheapest_shipping()
# What is the package_weight? --> Calc cheapest shipping
