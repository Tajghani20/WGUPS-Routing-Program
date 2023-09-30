# Truck class


class Truck:

    def __init__(self, location, time, time_departed_depot, capacity, speed, mileage, packages):
        """
        Truck constructor.

        :param str location: Truck location
        :param timedelta time: Current time
        :param timedelta time_departed_depot: departure time of the truck from depot
        :param int capacity: max number of packages in a truck
        :param int speed: MPH Truck speed
        :param float mileage: Distance travelled
        :param list packages: Currently on truck
        :returns None
        """
        self.location = location
        self.time = time
        self.time_departed_depot = time_departed_depot
        self.capacity = capacity
        self.speed = speed
        self.mileage = mileage
        self.packages = packages

    def __str__(self):
        """
        Truck string method.

        This method provides default syntax for Truck information (converts hashcode to string).

        :returns the truck description
        :rtype str
        """
        return ('Truck Location: %s, Current time: %s, Time Left Hub: %s, Capacity: %d, Speed: %d, Mileage: %.2f, '
                'Packages: %s ' %
                (self.location, self.time, self.time_departed_depot, self.capacity, self.speed, self.mileage, self.packages))