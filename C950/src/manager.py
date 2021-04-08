from truck import Truck
from global_file import *
from timeclass import Time

# Create truck objects
truck1 = Truck(1, locations[0])
truck2 = Truck(2, locations[0])
truck3 = Truck(3, locations[0])

#This class manages trucks
class Manager(object):
    def __init__(self, packages_hash_table):
        self.packages_hash_table = packages_hash_table

        #Truck dictionary
        self.trucks = {
            '1': truck1,
            '2': truck2,
            '3': truck3
        }
        #Package dictionary specifying which package to be loaded on which truck
        self.preset_packages = {
            '1': ['13', '14', '15', '16', '19', '20'],
            '2': ['3', '6', '18', '36', '38'],
            '3': ['9', '25', '28', '32']
        }

    def set_package_priority(self):
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N LOG N)
        for package in self.packages_hash_table.get_all_packages():
            if package.deadline == "9:00 AM":
                package.priority = 1
            elif package.deadline == "10:30 AM":
                package.priority = 2
            else:
                package.priority = 3
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)

    def run_simulation(self):
        #First load the packages in package_map due to restrictions
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N^2 LOG N)
        for truck in self.preset_packages.keys():
            current_truck = self.trucks[truck]
            package_ids = self.preset_packages[truck]
            for package_id in package_ids:
                package = self.packages_hash_table.get(package_id)
                package.truck = current_truck
                current_truck.load(package)

        #Now we load priority queues
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N^2 LOG N)
        for i in range(1, 4):
            for package in self.packages_hash_table.get_all_priority(i):
                if not truck1.is_full() and package.truck is None:
                    truck1.load(package)
                elif not truck2.is_full() and package.truck is None:
                    truck2.load(package)
                elif not truck3.is_full() and package.truck is None:
                    truck3.load(package)

        truck1.start_delivery(Time(8, 00))
        truck2.start_delivery(Time(8, 00))
        truck3.start_delivery(Time(10, 20))

        print_delivery_stats()
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2 LOG N)

    def show_ui(self):
        # SPACE | TIME COMPLEXITY:
        # O(1) | O(1)
        while True:
            task = input("\nEnter 'l' to look up package data "
                         "\nEnter 'i' to print all package data"
                         "\nEnter 'p' to print all package data at a given time"
                         "\nEnter 'r' to print package status of all packages between a time"
                         "\nEnter 'x' to exit program\n")
            if task == 'l':
                id = input("\nEnter a package id # you want to look up: ")
                print_package_data(self, id)
            elif task == 'i':
                print_all_package_data(self)
            elif task == 'p':
                print_status_at_time(self)
            elif task == 'r':
                time1 = input('Enter time in HH:MM format to query package statuses starting at: ')
                time2 = input('Enter time in HH:MM format to query package statuses ending at: ')
                times = [time1, time2]
                print_status_between_times(self, times)
            elif task == 'x':
                exit(0)
            else:
                print("Failed to provide appropriate input!")
        # TOTAL SPACE | TIME COMPLEXITY: O(1) | O(1)


def print_all_package_data(self):
    unsorted_packages = []
    # Go through every element in hash table
    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N^2)
    for i in range(0, len(self.packages_hash_table.table)):
        # Go through every element in that element (if it is empty len() will return 0)
        for j in range(0, len(self.packages_hash_table.table[i])):
            unsorted_packages.append(self.packages_hash_table.table[i][j])

    #We want a sorted list of packages so def a function which returns package.id for the sorted() function
    def sort_key(package):
        return int(package.id)
    sorted_packages = sorted(unsorted_packages, key=sort_key)

    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N)
    for package in sorted_packages:
        print(str(package))
        print("Left hub at: " + str(package.left_hub))
        print("Delivered at: " + str(package.delivered_at))
        print("")
    # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2)

def print_package_data(self, id):
    unsorted_packages = []
    # Go through every element in hash table
    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N^2)
    for i in range(0, len(self.packages_hash_table.table)):
        # Go through every element in that element (if it is empty len() will return 0)
        for j in range(0, len(self.packages_hash_table.table[i])):
            unsorted_packages.append(self.packages_hash_table.table[i][j])

    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N)
    for package in unsorted_packages:
        if package.id == id:
            print(str(package)
                  + "\nDelivery Address: " + str(package.delivery_address)
                  + "\nWeight: " + str(package.weight)
                  + "\nDeadline: " + str(package.deadline)
                  + "\nLeft Hub at: " + str(package.left_hub)
                  + "\nDelivered at: " + str(package.delivered_at)
                  + "\nWas loaded onto: " + str(package.truck))
            return
    print("Failed to find package with id: " + str(id))
    # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2)


def print_status_at_time(self):
    hours = 999
    query = input('Enter time in HH:MM format to query package statuses at a certain time: ')
    temp = query.split(':')
    hours = float(temp[0].strip())
    temp = temp[1].split(' ')
    minutes = float(temp[0].strip())
    time_requested = Time(hours, minutes)

    #Get all packages inside our hash table (it will be unsorted
    unsorted_packages = []

    #Go through every element in hash table
    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N^2)
    for i in range(0, len(self.packages_hash_table.table)):
        #Go through every element in that element (if it is empty len() will return 0)
        for j in range(0, len(self.packages_hash_table.table[i])):
            unsorted_packages.append(self.packages_hash_table.table[i][j])

    #Now we have to sort unsorted_packages by using sorted() function and key is the package id
    def sort_key(package):
        return int(package.id)
    sorted_packages = sorted(unsorted_packages, key=sort_key)

    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N)
    for package in sorted_packages:
        if time_requested < package.left_hub:
            print(str(package) + " status: AT HUB")
        elif package.left_hub < time_requested < package.delivered_at:
            print(str(package) + " status: IN TRANSIT")
        elif time_requested > package.delivered_at:
            print(str(package) + " status: DELIVERED")
        else:
            print("ERROR, ALL CASES FAILED!")
    # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2)


def print_status_between_times(self, times):
    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N)
    for i in range(0, 2):
        temp = times[i].split(':')
        hours = float(temp[0].strip())
        temp = temp[1].split(' ')
        minutes = float(temp[0].strip())
        if i == 0:
            time_1 = Time(hours, minutes)
        elif i == 1:
            time_2 = Time(hours, minutes)

    # Get all packages inside our hash table (it will be unsorted
    unsorted_packages = []
    # Go through every element in hash table
    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N^2)
    for i in range(0, len(self.packages_hash_table.table)):
        # Go through every element in that element (if it is empty len() will return 0)
        for j in range(0, len(self.packages_hash_table.table[i])):
            unsorted_packages.append(self.packages_hash_table.table[i][j])

    # Now we have to sort unsorted_packages by using sorted() function and key is the package id
    def sort_key(package):
        return int(package.id)

    sorted_packages = sorted(unsorted_packages, key=sort_key)
    # SPACE | TIME COMPLEXITY:
    # O(N) | O(N)
    for package in sorted_packages:
        if time_1 <= package.delivered_at <= time_2 :
            print(str(package) + " status: DELIVERED BETWEEN TIMES")
        elif time_1 >= package.delivered_at:
            print(str(package) + " status: ALREADY DELIVERED")
        elif time_2 <= package.left_hub:
            print(str(package) + " status: STILL IN HUB")
        elif time_1 <= package.left_hub <= time_2:
            print(str(package) + " status: LEFT HUB BETWEEN TIMES")
        elif time_1 >= package.left_hub and time_2 < package.delivered_at:
            print(str(package) + " status: IN TRANSIT")
        else:
            print(str(package) + "ERROR with times: " + str(package.left_hub) + " | " + str(package.delivered_at))
    # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2)


def print_delivery_stats():
    #SPACE | TIME COMPLEXITY:
    # O(1) | O(1)
    total_miles = truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled
    total_minutes = truck1.time_traveling + truck2.time_traveling + truck3.time_traveling
    total_hours = total_minutes // 60
    total_minutes = (total_minutes - (total_hours * 60))
    print("Combined miles: " + str(total_miles.__round__(3)) + " \nAnd took a total time of "
          + str(int(total_hours)) + " hours and " + str(int(total_minutes)) + " minutes")
    # TOTAL SPACE | TIME COMPLEXITY: O(1) | O(1)


