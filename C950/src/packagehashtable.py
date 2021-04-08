from chaininghashtable import ChainingHashTable
from package import Package
from global_file import *

class PackageHashTable(ChainingHashTable):
    def __init__(self, initial_capacity=40):
        super().__init__(initial_capacity)

    #Insert package into hash table
    def insert(self, package_id, street, city, zip_code, weight, deadline):
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N)
        for current_location in locations:
            if current_location.street == street and current_location.city == city and current_location.zip_code == zip_code:
                package = Package(package_id, current_location, weight, deadline)
                return super().insert(package) #Package into parents insert function
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)


    def get(self, package_id):
        return super().get(package_id)

    def get_all_packages(self):
        all_packages = []
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N)
        for element in self.table:
            for package in element:
                all_packages.append(package)
        return all_packages
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)

    def get_all_priority(self, priority_level):
        all_packages = []
        # SPACE | TIME COMPLEXITY:
        # O(N)  | O(N^2)
        for element in self.table:
            for package in element:
                if package.priority == priority_level:
                    all_packages.append(package)
        return all_packages
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N^2)
