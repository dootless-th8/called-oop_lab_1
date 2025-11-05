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

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

# Template for using filter
# ger_filtered = filter(lambda x: x['country']=="Germany", cities)
# print(ger_filtered)

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temp = []
    for i in dict_list:
        temp.append(i[aggregation_key])
    return aggregation_function(temp)
            

# Print all cities in Germany
print("All Germans")
ger_filtered = filter(lambda x: x['country']=="Germany", cities)
for i in ger_filtered:
    print(i)
# germans = []
# for cit in cities:
#     if cit['country'] == 'Germany':
#         germans.append(float(cit['temperature']))
#         print(cit)


# Print all cities in Spain with a temperature above 12°C
print("\nPrint all cities in Spain with a temperature above 12°C")
sp_filtered = filter(lambda x:x['country'] == "Spain" and float(x['temperature']) > 12, cities)
for i in sp_filtered:
    print(i)
# for cit in cities:
#     if cit['country'] == 'Spain' and float(cit['temperature']) > 12:
#         print(cit)


# Count the number of unique countries
print("\nCount the number of unique countries:")
unique = aggregate('country', lambda x:len(set(x)), cities)
print(unique)
# uni_count = []
# stack = 0
# for cit in cities:
#     if cit['country'] not in uni_count:
#         stack += 1
#         uni_count.append(cit['country'])
# print(stack)


# # Print the average temperature for all the cities in Germany
print("\nPrint the average temperature for all the cities in Germany")
fil_ger = filter(lambda x:x['country'] == "Germany", cities)
tota = aggregate('temperature', lambda x: [float(i) for i in x], fil_ger)
print( sum(tota)/len(tota) )
# total = sum(germans)
# print(f"Average: {total/len(germans)}")


# Print the max temperature for all the cities in Italy
print("\nPrint the max temperature for all the cities in Italy")
fil_ita = filter(lambda x:x['country'] == "Italy", cities)
ita_max_temp = aggregate('temperature', lambda x:[float(i) for i in x], fil_ita)
print(max(ita_max_temp))

# ita = []
# for cit in cities:
#     if cit['country'] == 'Italy':
#         ita.append(float(cit['temperature']))
# print(f"Max temp in Italia: {max(ita)}")
