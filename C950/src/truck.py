from global_file import *
from timeclass import Time

class Truck(object):
    def __str__(self):
        return "Truck" + str(self.id)

    def __init__(self, truck_id, start_location):
        self.id = truck_id
        self.avg_speed = 18.0
        self.max_capacity = 16
        self.packages_loaded = []
        self.start_location = start_location
        self.current_location = start_location
        self.distance_traveled = 0.0

        #in minutes
        self.time_traveling = 0.0
        self.current_time = None

    def load(self, package):
        #Load package but make sure its not already loaded
        # SPACE | TIME COMPLEXITY:
        # O(1) | O(1)
        if not self.packages_loaded.__contains__(package):
            package.truck = self
            self.packages_loaded.append(package)
        # TOTAL SPACE | TIME COMPLEXITY: O(1) | O(1)

    def is_full(self):
        return len(self.packages_loaded) == self.max_capacity

    def start_delivery(self, time):
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N)
        for package in self.packages_loaded:
            package.left_hub = Time(time.hour, time.minute)
        self.current_time = time
        print(str(self) + " is leaving at " + str(self.current_time) + " and has a total of " + str(len(self.packages_loaded)) + " packages")

        #Go through all packages loaded
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N)
        while len(self.packages_loaded) != 0:
            self.deliver_package()


        #Once we are done delivering all packages
        print(str(self) + " has finished delivery at " + str(self.current_time) + " with a total of " + str(self.distance_traveled.__round__(2)) + " miles")
        print("")
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)

    def deliver_package(self):
        lowest_distance = 9999  # initialize to a really high number so we can beat it
        #Go through the priority list (starts with 1 and ends with 3)
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N)
        for package in self.return_highest_priority_packages():
            #Find the closest package we can deliver
            if return_distance(self.current_location, package.delivery_address) < lowest_distance:
                lowest_distance = return_distance(self.current_location, package.delivery_address)
                pop_index = self.packages_loaded.index(package)
        closest_package = self.packages_loaded[pop_index]

        #Once we go through every package and find the closest one we can now deliver it and set stats
        time_to_next_stop = (lowest_distance / self.avg_speed) * 60
        self.distance_traveled += lowest_distance
        self.time_traveling += time_to_next_stop
        self.current_time.add(time_to_next_stop)
        closest_package.delivered_at = Time(self.current_time.hour, self.current_time.minute)

        print('Truck{} traveling from {} -> {}, it will travel {} miles and should take {} minutes to get there and arrive at {}'.format(
                self.id, self.current_location, self.packages_loaded[pop_index].delivery_address, lowest_distance,
                time_to_next_stop.__round__(2), str(self.current_time)))
        #if closest_package.priority < 3:
        #    print("         {} has a deadline at {}, it was delivered at {}.".format(closest_package, closest_package.deadline, closest_package.delivered_at))
        # Pop the package out of the loaded packages
        self.current_location = self.packages_loaded.pop(pop_index).delivery_address
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)

    #Returns a list of packages starting with highest_priority (i.e. we will return packages with priority 1 and then 2)
    def return_highest_priority_packages(self):
        priority_packages = []
        #Go through all the priorities starting with 1 and ending with 3
        # SPACE | TIME COMPLEXITY:
        # O(N)  | O(N^2)
        for i in range(1, 4):
            #We go through all the packages loaded
            for package in self.packages_loaded:
                #If we find any package with the given priority add it to the list
                if package.priority == i:
                    priority_packages.append(package)
            #Once we are done going through all packages check and see if any were added
                #Else move onto next priority
            if len(priority_packages) > 0:
                break
        return priority_packages
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2)


def return_distance(current_location, target_location):
    #SPACE | TIME COMPLEXITY:
    # O(1) | O(1)
    current_index = locations.index(current_location)
    target_index = locations.index(target_location)
    distance = distances[current_index][target_index]
    return distance
    # TOTAL SPACE | TIME COMPLEXITY: O(1) | O(1)

