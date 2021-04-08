from dataLoader import DataLoader

#Global variables to be accessed between files.
global data_loader
data_loader = DataLoader()

global locations
locations = data_loader.setup_locations()

global distances
distances = data_loader.setup_distances()

global all_packages
all_packages = data_loader.setup_packages(locations)
