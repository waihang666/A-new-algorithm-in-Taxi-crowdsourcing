from flask import make_response, jsonify
import geopy.distance

def wrap_response(data, error_code, error_msg):
    return make_response(jsonify({"data": data, "error_code": error_code, "error_message": error_msg}))

def get_latitude_longitude_limit(distance, latitude, longitude):
    north = geopy.distance.distance(kilometers=distance).destination((latitude, longitude), bearing=0)
    east = geopy.distance.distance(kilometers=distance).destination((latitude, longitude), bearing=90)
    south = geopy.distance.distance(kilometers=distance).destination((latitude, longitude), bearing=180)
    west = geopy.distance.distance(kilometers=distance).destination((latitude, longitude), bearing=270)
    return ((south[0], north[0]), (west[1], east[1]))

def get_begin_index_by_latitude(data, latitude):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        # print(data[mid].latitude)
        if latitude > data[mid].latitude:
            low = mid + 1
        elif latitude < data[mid].latitude:
            high = mid - 1
        else:
            return mid
    if low < 0:
        return 0
    else:
        return low

def get_end_index_by_latitude(data, latitude):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        # print(data[mid].latitude)
        if latitude > data[mid].latitude:
            low = mid + 1
        elif latitude < data[mid].latitude:
            high = mid - 1
        else:
            return mid
    if low >= len(data):
        return len(data) -1
    else:
        return low

def filter_spots_by_latitude_longitude_range(data, distance, latitude, longitude):
    print(len(data))
    latitude_longitude_range = get_latitude_longitude_limit(distance, latitude, longitude)
    begin_index = get_begin_index_by_latitude(data, latitude_longitude_range[0][0])
    print(latitude_longitude_range)
    end_index = get_end_index_by_latitude(data, latitude_longitude_range[0][1])
    print(begin_index, end_index)
    result = [(data[i].longitude, data[i].latitude) for i in range(begin_index, end_index)
              if latitude_longitude_range[1][0] <= data[i].longitude <= latitude_longitude_range[1][1]]
    return result

