from manager import Manager
from global_file import *
from packagehashtable import PackageHashTable

#Joseph Demyanovskiy 001208427

def main():
    packages_hash_table = create_package_hash()

    #Create truck manager and use
    manager = Manager(packages_hash_table)
    manager.set_package_priority()
    manager.run_simulation()
    manager.show_ui()

#Goes through every item in all_packages list and inserts them into hash table
def create_package_hash():
    packages_hash_table = PackageHashTable()
    #SPACE | TIME COMPLEXITY:
    # O(N) | O(N)
    for item in all_packages:
        package_id = item['package_id']
        delivery_address = item['delivery_address']
        city = item['city']
        zip_code = item['zip_code']
        weight = item['weight']
        deadline = item['deadline']
        packages_hash_table.insert(package_id, delivery_address, city, zip_code, weight, deadline)
    return packages_hash_table
    # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)


main()

