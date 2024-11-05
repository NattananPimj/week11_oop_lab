import csv, os


class Database:
    def __init__(self, data: str):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.dict_list = []
        with open(os.path.join(__location__, data)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.dict_list.append(dict(r))

    def filter(self, condition):
        filtered_list = []
        for item in self.dict_list:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_key):
        values = []
        for items in self.dict_list:
            values.append(float(items[aggregation_key]))
        return values


class Country:
    def __init__(self, city, data):
        self.data = Database(data)
        self.cities = self.data.filter(lambda x: x['country'] == city)

    def num_aggregate(self, aggregation_key):
        values = []
        for items in self.cities:
            values.append(float(items[aggregation_key]))
        return values

    def aggregate(self, aggregation_key):
        values = []
        for items in self.cities:
            values.append(items[aggregation_key])
        return values

    def max_value(self, key):
        if self.check_nodata():
            return "There is no data"
        return max(self.num_aggregate(key))

    def min_value(self, key):
        if self.check_nodata():
            return "There is no data"
        return min(self.num_aggregate(key))

    def mean_value(self, key):
        if self.check_nodata():
            return "There is no data"
        return sum(self.num_aggregate(key)) / len(self.cities)

    def check_nodata(self):
        return len(self.cities) == 0



# main

# Print the average temperature of all the cities
cities = Database('Cities.csv')
print(cities.aggregate('temperature'))

# Print all cities in Italy
italy = Country('Italy', 'Cities.csv')
print(italy)
print(italy.aggregate('city'))

# Print the average temperature for all the cities in Italy
print(italy.mean_value('temperature'))

# Print the max temperature for all the cities in Italy
print(italy.max_value('temperature'))

# Print the min temperature for all the cities in Italy
print(italy.min_value('temperature'))

sweden = Country('Swedish', 'Cities.csv')
# - print the average temperature for all the cities in Sweden
print(sweden.mean_value('temperature'))

# - print the max temperature for all the cities in Sweden
print(sweden.max_value('temperature'))

# - print the min temperature for all the cities in Sweden
print(sweden.min_value('temperature'))
