import csv
from location import Location

class DataLoader(object):
    def setup_distances(self):
        def convert_to_float(distance_str):
            distance = float(distance_str.strip())
            return distance

        file = "data/distances.csv"
        distances_data = [] #main list of distances (every index is a row in distances.csv)
        with open(file, newline='', encoding='utf-8-sig') as distances_file:
            reader = csv.reader(distances_file)
            # SPACE | TIME COMPLEXITY:
            # O(N) | O(N)
            for row in reader:
                current_row = list(map(convert_to_float, list(row))) #set current row to the row we are on in the reader
                distances_data.append(current_row) #add current row to the main list of distances
        return distances_data
        #TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)

    #Setups list of all package objects
    def setup_packages(self, locations):
        file = "data/packages.csv"
        all_packages = []
        with open(file, newline='', encoding='utf-8-sig') as packages_file:
            reader = csv.reader(packages_file)
            # SPACE | TIME COMPLEXITY:
            # O(N) | O(N)
            for row in reader:
                new_package = {
                    'package_id': row[0].strip(),
                    'delivery_address': row[1].strip(),
                    'city': row[2].strip(),
                    'zip_code': row[4].strip(),
                    'weight': row[5].strip(),
                    'deadline': row[6].strip()
                }
                all_packages.append(new_package)
        return all_packages
        #TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)

    #Creates list of all location objects
    def setup_locations(self):
        file = "data/locations.csv"
        list_of_locations = []

        with open(file, newline='', encoding='utf-8-sig') as locations_file:
            reader = csv.reader(locations_file)
            # SPACE | TIME COMPLEXITY:
            # O(N) | O(N)
            for row in reader:
                location = Location(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip())
                list_of_locations.append(location)
        return list_of_locations
        #TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)
