from init import spots, app
from flask import request
import config
from util import wrap_response, filter_spots_by_latitude_longitude_range

@app.route('/api/crowdsourcinglogistics/getpoi_by_longlat', methods=["POST", "GET"])
def search_by_sequence():
    try:
        longitude = request.form["longtitude"]
        latitude = request.form["latitude"]
        print(f"Incoming new request for POI of (latitude: {latitude}, longitude:{longitude})")
        result = filter_spots_by_latitude_longitude_range(spots, config.POI_DISTANCE, latitude, longitude)

        if len(result) == 0:
            print("no result")
            return wrap_response([], 201, "no POI found")
        else:
            result = [{"longitude": i[0], "latitude": i[1]} for i in result]
            print(f"一共获取 {len(result)} 个POI")
            return wrap_response(result, 0, "POI found")
    except Exception as e:
        print(e)
        return wrap_response([], 500, str(e))

if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)

