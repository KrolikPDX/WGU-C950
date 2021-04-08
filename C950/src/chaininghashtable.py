class ChainingHashTable(object):
    def __init__(self, capacity=40):
        self.table = []
        #Go through the capacity of the table and just set it to empty (need to do this create key with len(table))
        for i in range(capacity):
            self.table.append([])

    #Inserts into hash table
    def insert(self, package):
        #YouTube tutorial recommended to simply hash(package_object) and then modulo the length of table for the index
        # SPACE | TIME COMPLEXITY:
        # O(1) | O(1)
        bucket_index = hash(package) % len(self.table)
        bucket_list = self.table[bucket_index]
        bucket_list.append(package)
        # TOTAL SPACE | TIME COMPLEXITY: O(1) | O(1)

    #Search through hash map to find our package
    def get(self, package_id):
        #Get index where to store item
        bucket_index = hash(str(package_id)) % len(self.table)
        bucket_list = self.table[bucket_index]
        # SPACE | TIME COMPLEXITY:
        # O(N) | O(N)
        for package in bucket_list:
            if int(package.id) == int(package_id):
                return package
        # TOTAL SPACE | TIME COMPLEXITY: O(N) | O(N)




