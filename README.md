# This program is about processing data containing temperature, longtitude, and latitude from different cities within Europe

### oop_lab_1/
* │
* ├── README.md                 # This file
* ├── Cities.csv                      # The dataset
 * |---- data_processing.py	  # The analysis code

## Methods;
#### Class Dataloader:
* ##### DataLoader is for transfering .csv file into each text lines from respective path, then collecting them in dictionary.
    * ##### Method __init__(self, base_path=None): Initialize the DataLoader with a base path for data files. 
    * ##### Method load_csv(self, filename): Load a CSV file and return its contents as a list of dictionaries.

#### Class Table:
* ##### Table is for handling the good stuffs. 
    * ##### Method __init__(self, key, dic): Initialize data in dictionary format.
    * ##### Method aggregate(self, aggregation_function, aggregation_key): As the name suggest, aggregate as the requirement according to the aggregation_function which required lambda buli-in methods to process the operation.
    * ##### filter(self, condition): Just filtering all the data and return value as Table object as propmt via condition using lambda method.

## Run the program
#### First, make three variables such as 'loader' for Dataloader, 'cities' for getting all the goods from the 'Cities.csv' file then create a "Table" object out of 'cities'. Anything else just experiment with it just that it is reccomended to use lambda to make use the best out of this program.
