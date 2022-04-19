import csv


def sep_spots():
    f_1 = open("西城区poi.csv", "w", encoding="utf8")
    f_2 = open("东城区poi.csv", "w", encoding="utf8")
    f = open("北京市poi.csv", "r", encoding="utf8")
    lines = f.readlines()
    with open("北京市poi.csv", encoding="utf") as file:
        reader = csv.reader(file, delimiter=",")
        for i, row in enumerate(reader):
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
            if district == "东城区":
                f_2.write(lines[i])
            elif district == "西城区":
                f_1.write((lines[i]))
    f_1.close()
    f_2.close()

if __name__ == "__main__":
    sep_spots()