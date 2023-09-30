#Author: Tajuddin AbdulGhani
#Student ID: 010558415
#Title: WGUPS Delivery Application


import HashTable
import Truck
import CSVReader
import datetime


def distance_in_between(add1, add2, address_data, distance_data):
    # Distance in between two addresses method
    # returns float distance value
    # Distance initialized to 0
    distance = 0
    # determines index of address string value
    h = address_data.index(add1)
    # determines index of second address string value
    j = address_data.index(add2)
    # Searches 2-D distance data list
    # If value returned is '', indexes are swapped
    if distance_data[h][j] == '':
        distance = distance_data[j][h]
    else:
        distance = distance_data[h][j]
    # Returns float distance value
    return float(distance)


def min_distance_from(curr_address, pkg_list, hash_table, address_data, distance_data):
    # Minimum distance method Determines which package address in list is the closest from the current address
    # Returns the closest package address, the associated package id, and the distance b/w that address and current
    # address Give minimum distance, next address, and next package id initial values
    min_distance = 1000
    next_address = ''
    next_id = 0
    # print('Determining the Closest Address!')
    # Search package list for minimum distance
    for pkg_id in pkg_list:
        # searches package hash table for object, based on package id from package list
        pkg = hash_table.search(pkg_id)
        # assigns current package address to temporary value
        address2 = pkg.address
        # Call distance in between method
        # Determine distance between current address and temporary package address
        distance = distance_in_between(curr_address, address2, address_data, distance_data)
        # print('Package ID: %d Distance: %.1f' % (pkg_id, distance))
        # If the temporary package address is 0 miles away, then this is the closest address
        if distance == 0:
            min_distance = distance  # new minimum distance
            next_address = address2  # new closest address
            next_id = pkg.package_id  # package ID associated with the closest address
            # print('Closest Package Details: ID: %d Address: %s Distance: %.1f' % (next_id, next_address,
            # min_distance)) print() return closest address and associated values
            return next_address, next_id, min_distance
        # If distance is not 0, but less than current minimum distance, then new minimum is assigned
        elif distance < min_distance:
            min_distance = distance  # new minimum distance
            next_address = address2  # new closest address
            next_id = pkg.package_id  # package ID associated with the closest address
    # print('Closest Package Details: ID: %d Address: %s Distance: %.1f' % (next_id, next_address, min_distance))
    # print()
    # return closest address and associated values
    return next_address, next_id, min_distance


def load_truck_packages(truck1, truck2, truck3):
    # Manually Load Packages to truck method
    list1 = [1, 2, 5, 7, 10, 13, 14, 15, 16, 19, 20, 29, 33, 34, 37, 39]
    list2 = [3, 6, 8, 11, 12, 18, 23, 25, 27, 30, 31, 35, 36, 38, 40]
    list3 = [4, 9, 17, 21, 22, 24, 26, 28, 32]
    truck1.packages = list1
    truck2.packages = list2
    truck3.packages = list3

    # print('Truck 1 is Loaded:', list1)
    # print('Truck 2 is Loaded:', list2)
    # print('Truck 3 is Loaded:', list3)
    # print()

    # DELIVERY CONSTRAINTS
    # Can only be on truck 2: 3, 18, 36, 38
    # Must be on the SAME truck: 13, 14, 15, 16, 19, 20
    # Delayed on Flight (will not arrive to hub until 09:05:00): 6, 25, 28, 32
    # Wrong address listed (correct address arrives at 10:20:00): 9 (correct address: 410 S State St)
    # 10:30:00 Deadline: 1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40
    # 09:00:00 Deadline: 15
    """
        print('10:30:00 Deadline:')
        print(p_hash_table.search(1))
        print(p_hash_table.search(6))
        print(p_hash_table.search(13))
        print(p_hash_table.search(14))
        print(p_hash_table.search(16))
        print(p_hash_table.search(20))
        print(p_hash_table.search(25))
        print(p_hash_table.search(29))
        print(p_hash_table.search(30))
        print(p_hash_table.search(31))
        print(p_hash_table.search(34))
        print(p_hash_table.search(37))
        print(p_hash_table.search(40))
        print()
        print('09:00:00 Deadline:')
        print(p_hash_table.search(15))
    """


def deliver_truck_packages(truck, time, hash_table, address_data, distance_data):
    # Deliver truck packages method
    # Delivered packages list instance
    delivered = []
    # Not delivered packages list instance
    not_delivered = truck.packages.copy()
    # Set current address to truck location (hub)
    curr_address = truck.location
    # Total distance traveled
    distance_traveled = 0
    # Creates time object for truck start time
    start_time = time
    h, m, s = start_time.split(':')
    time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    # Until 'not delivered' package list is empty, packages are delivered
    while len(not_delivered) > 0:
        # Package delivery status' are changed to 'En route'
        for pkg in not_delivered:
            # Update package status
            curr_pkg = hash_table.search(pkg)
            curr_pkg.status = 'En route'
            # print('Package ID:', curr_pkg.package_id, 'Status:', curr_pkg.status)
        # print()
        # Deliver all packages based on package address distance
        # Update distance traveled, package status, current and delivery times throughout process
        for pkg in not_delivered:
            # print('Delivered:', delivered)
            # print('Not Delivered:', not_delivered)
            # print()
            # Call minimum distance from current address method
            # Determine the closest address
            address, pkg_id, miles = min_distance_from(curr_address, not_delivered, hash_table, address_data,
                                                       distance_data)
            curr_address = address
            # Update distance traveled
            distance_traveled += miles
            # print('Total Distance traveled:', distance_traveled)
            if miles == 0:
                # print('Current time:', time_object)
                # Update package status
                curr_pkg = hash_table.search(pkg_id)
                curr_pkg.status = 'Delivered at ' + str(time_object)
            else:
                # Update time
                time_passed = (miles / 18) * 60 * 60
                dts = datetime.timedelta(seconds=int(time_passed))
                time_object += dts
                # print('Current time:', time_object)
                # Update package status
                curr_pkg = hash_table.search(pkg_id)
                curr_pkg.status = 'Delivered at ' + str(time_object)
            # Add package to delivered list
            delivered.append(pkg_id)
            # Update package start and delivery time
            curr_pkg = hash_table.search(pkg_id)
            curr_pkg.truck_start_time = truck.time_departed_depot
            curr_pkg.delivery_time = time_object
            # Remove package from not delivered list
            not_delivered.remove(pkg_id)
            # Print delivered package
            # print('Package', curr_pkg.package_id, 'Delivered!')
            # Update truck information
            truck.location = curr_address
            truck.time = time_object
            truck.mileage = distance_traveled
            # print(truck)
            # print()
    # All packages have been delivered. Time to return to the hub.
    # Final stop
    # print('Last stop: The hub!')
    hub = '4001 South 700 East'
    # Calculate distance between current truck location and the hub
    miles = distance_in_between(truck.location, hub, address_data, distance_data)
    # print('Distance to hub:', miles)
    # print('Distance traveled thus far:', distance_traveled)
    # Update distance traveled
    distance_traveled += miles
    # print('Final truck mileage:', distance_traveled)
    # Update truck miles
    truck.mileage = distance_traveled
    time_passed = (miles / 18) * 60 * 60
    dts = datetime.timedelta(seconds=int(time_passed))
    time_object += dts
    # Update truck time
    truck.time = time_object
    # Update truck location
    truck.location = hub
    # print('Delivery Completed!')
    # print('Delivered:', delivered)
    # print('Not Delivered:', not_delivered)
    # print(truck)
    # print()
    # Return final truck mileage
    return truck.mileage


def command_user_interface(truck1, truck2, truck3, hash_table):
    user_input = 9
    total_miles = truck1.mileage + truck2.mileage + truck3.mileage
    while user_input != 3:
        # Command UI Main Menu
        print('*' * 50)
        print('Total miles travelled by all trucks: %.1f' % total_miles)
        print('*' * 50)
        print('Please select an option below: ')
        print('1) Single package lookup')
        print('2) All packages')
        print('3) Exit the Program \n')
        user_input = int(input())
        if user_input == 1:
            # Specific Package Information (by Package ID)
            # print('Option 1 was selected!')
            print('Please input a Package ID ')
            user_input = int(input())
            # print('Package ID chosen:', user_input)
            print(hash_table.search(user_input))
            print()
        elif user_input == 2:
            # Specific Package Information (by Time)
            # print('Option 2 was selected!')
            print('Please input the time (HH:MM:SS)')
            user_input = input()
            (h, m, s) = user_input.split(':')
            convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            print('All Package details:', convert_user_time)
            for p_id in range(1, 41):
                pkg = hash_table.search(p_id)
                print(pkg.print_status_for_time(convert_user_time))
            print()
        elif user_input == 3:
            # Exit Program
            print('You have chosen to \'exit\' the program.')
            print('Goodbye.')


def main():
    # Main method

    # Hash table instance
    p_hash_table = HashTable.HashTable()
    # Distance List instance
    distance_data = []
    # Address List instance
    address_data = []

    # Load Packages to Hash Table
    CSVReader.load_package_data('CSV/Package Table.csv', p_hash_table)
    # Load Distances to 2-D List
    CSVReader.load_distance_data('CSV/Distance Table.csv', distance_data)
    # Load Addresses to List
    CSVReader.load_address_data('CSV/Address Table.csv', address_data)

    # Instantiate Truck Objects
    hub = '4001 South 700 East'
    list1 = []
    list2 = []
    list3 = []
    truck1 = Truck.Truck(hub, '08:00:00', '08:00:00', 16, 18, 0, list1)
    truck2 = Truck.Truck(hub, '09:05:00', '09:05:00', 16, 18, 0, list2)
    truck3 = Truck.Truck(hub, '10:20:00', '10:20:00', 16, 18, 0, list3)

    # Load Packages to Trucks
    # print('Loading Packages!')
    load_truck_packages(truck1, truck2, truck3)

    # Deliver Truck Packages
    # print('Truck 1 Delivery Started!')
    deliver_truck_packages(truck1, truck1.time_departed_depot, p_hash_table, address_data, distance_data)
    # print('Truck 2 Delivery Started!')
    deliver_truck_packages(truck2, truck2.time_departed_depot, p_hash_table, address_data, distance_data)
    # print('Truck 3 Delivery Started!')
    # Change package #9 delivery address
    pkg_9 = p_hash_table.search(9)
    pkg_9.address = '410 S State St'
    deliver_truck_packages(truck3, truck3.time_departed_depot, p_hash_table, address_data, distance_data)

    """
    # ALL Truck Information
    # Truck Packages (at start)
    print('Truck Packages (at start):')
    print('Truck 1 Packages:', truck1.packages)
    print('Truck 2 Packages:', truck2.packages)
    print('Truck 3 Packages:', truck3.packages)
    print()
    # Truck Times
    print('Truck Delivery Times:')
    print('Truck 1 start time:', truck1.time_left_hub)
    print('Truck 1 completion time:', truck1.time)
    print('Truck 2 start time:', truck2.time_left_hub)
    print('Truck 2 completion time:', truck2.time)
    print('Truck 3 start time:', truck3.time_left_hub)
    print('Truck 3 completion time:', truck3.time)
    print()
    # Total miles traveled
    print('Truck Miles:')
    t1_miles = '%.1f' % truck1.mileage
    print('Truck 1 Miles:', t1_miles)
    print('Truck 2 Miles:', truck2.mileage)
    print('Truck 3 Miles:', truck3.mileage)
    total_miles = '%.1f' % (truck1.mileage + truck2.mileage + truck3.mileage)
    print('Total Miles:', total_miles)
    print()
    """

    # Command UI
    command_user_interface(truck1, truck2, truck3, p_hash_table)


if __name__ == '__main__':
    main()

