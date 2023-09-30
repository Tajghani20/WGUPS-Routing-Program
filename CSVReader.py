# 'Read CSV' file
import csv

from Package import Package


def load_package_data(file_name, hash_table):
    # Load package data from csv file method
    # Insert values from csv file into key/value pairs of the hash table
    with open(file_name) as Package_file:
        package_data = csv.reader(Package_file, delimiter=',')
        for package in package_data:
            p_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = float(package[6])
            status = 'At the hub'

            # Package object
            p = Package(p_id, address, city, state, zipcode, deadline, weight, status)

            # Insert object into hash table
            hash_table.insert(p_id, p)


def load_address_data(file_name, address_data):
    # Load address data from csv file method
    # Insert address value from csv file into list
    with open(file_name) as address_file:
        addresses = csv.reader(address_file, delimiter=",")
        for address in addresses:
            address_data.append(address[2])


def load_distance_data(file_name, distance_data):
    # Load distance data from csv file method
    # Insert distance values from csv file into 2-D list
    with open(file_name) as distance_file:
        distances = csv.reader(distance_file, delimiter=",")
        for distance in distances:
            distance_data.append(distance)


def print_package_table(hash_table):
    # Print package table method
    # Prints package objects
    for i in range(len(hash_table.table)):
        # Calls hash table search method
        print("{}".format(hash_table.search(i + 1)))
