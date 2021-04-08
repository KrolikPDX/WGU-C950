# WGU-C950
Course work for WGU's course C950. This application uses Python to simulate delivery times using distance data and the nearest neighbor algorithm. 

## Overview
Below is the state problem provided by WGU. Our goal is to create an app that will simulate a package shipping environment with certain assumptions and restrictions. This project incorportates:

- Python
- CSV file parsing
- Data hashing
- Nearest neightbor algorithm
- Delivery time and mile count
- Space-time complexity evaluation using Big O notation

### Stated Problem
The purpose of this project is to create an algorithm for the Western Governors University Parcel Service (WGUPS) to determine the best route and delivery distribution for their Salt Lake City Daily Local Deliveries (DLD). Packages are currently not being delivered by their promised deadline and a more efficient and accurate solution is necessary. The Salt Lake City route is covered by three trucks, two drivers, and has a daily average of approximately 40 packages.

#### Assumptions:
The following are the constraints imposed on the WGUPS delivery service:

- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Trucks have a “infinite amount of gas” with no need to stop.
- Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
- Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
- There is up to one special note for each package.
- The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
- The package ID is unique; there are no collisions.
- No further assumptions exist or are allowed.

#### Restrictions
Each package may have **one** special requirement that must be addressed by the WGUPS. The following are possible restrictions that may be imposed on a given package:

- The package must be delivered with other packages.
  - We refer to these packages as _linked_ packages in our algorithm.
- The package must be delivered by a specific truck.
- The package has a specific deadline by which it must be delivered.
- The package is delayed in arriving to the depot and will not be available for pickup until later in the day.

## Getting Started
### Prerequisites
- PyCharm
- Downloaded and installed current version of python

### Installation
1. Clone or download the project to your local machine.
2. Open the project through your IDE.
3. Make sure your python interpreter is set by going to `Run > Edit Configurations > Main`. Go to the 'Python Interpreter' tab and select your python version. 
4. Build and run

#### Side notes
The annotations and screenshots are included which are required for submission of the project.  

## Links
- [PyCharm IDE] -> https://www.jetbrains.com/pycharm/
- [Python] -> https://www.python.org/downloads/
