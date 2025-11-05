import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All Germans")
germans = []
for cit in cities:
    if cit['country'] == 'Germany':
        germans.append(float(cit['temperature']))
        print(cit)


# Print all cities in Spain with a temperature above 12°C
print("\nPrint all cities in Spain with a temperature above 12°C")
for cit in cities:
    if cit['country'] == 'Spain' and float(cit['temperature']) > 12:
        print(cit)


# Count the number of unique countries
print("\nCount the number of unique countries")
uni_count = []
stack = 0
for cit in cities:
    if cit['country'] not in uni_count:
        stack += 1
        uni_count.append(cit['country'])
print(stack)


# Print the average temperature for all the cities in Germany
print("\nPrint the average temperature for all the cities in Germany")
total = sum(germans)
print(f"Average: {total/len(germans)}")


# Print the max temperature for all the cities in Italy
print("\nPrint the max temperature for all the cities in Italy")
ita = []
for cit in cities:
    if cit['country'] == 'Italy':
        ita.append(float(cit['temperature']))
print(f"Max temp in Italia: {max(ita)}")
