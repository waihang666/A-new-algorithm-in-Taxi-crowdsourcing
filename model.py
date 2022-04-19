import csv
import config
class Spot:
    def __init__(self, index, name, location, latitude, longitude, city, district, type1, type2, contact_no=None):
        self.index = index
        self.name = name
        self.location = location
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.district = district
        self.type1 = type1
        self.type2 = type2
        self.contact_no = contact_no

def load_spots():
    with open(config.data_file, encoding="utf") as file:
        reader = csv.reader(file, delimiter=",")
        spots = []
        for row in reader:
            index = int(row[0])
            name = row[1]
            location = row[2]
            latitude = float(row[3])
            longitude = float(row[4])
            city_and_district = row[5].split(";")
            city = city_and_district[0]
            district = city_and_district[1]
            type_1_2 = row[6].split(";")
            type1 = type_1_2[0]
            type2 = type_1_2[1]
            contact_no = row[7]
            spot = Spot(index, name, location, latitude, longitude, city, district, type1, type2, contact_no)
            spots.append(spot)
        return spots