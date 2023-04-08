import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import ValidationError

from schema.MeasurementSchema import MeasurementsSchema

app = Flask(__name__)
CORS(app)

temp_intervals = {pd.Interval(left=31, right=35, closed='right'): 3,
                  pd.Interval(left=35, right=36, closed='right'): 1,
                  pd.Interval(left=36, right=38, closed='right'): 0,
                  pd.Interval(left=38, right=39, closed='right'): 1,
                  pd.Interval(left=39, right=42, closed='right'): 2}

hr_intervals = {pd.Interval(left=25, right=40, closed='right'): 3,
                pd.Interval(left=40, right=50, closed='right'): 1,
                pd.Interval(left=50, right=90, closed='right'): 0,
                pd.Interval(left=90, right=110, closed='right'): 1,
                pd.Interval(left=110, right=130, closed='right'): 2,
                pd.Interval(left=130, right=220, closed='right'): 3}

rr_intervals = {pd.Interval(left=3, right=8, closed='right'): 3,
                pd.Interval(left=8, right=11, closed='right'): 1,
                pd.Interval(left=11, right=20, closed='right'): 0,
                pd.Interval(left=20, right=24, closed='right'): 2,
                pd.Interval(left=24, right=60, closed='right'): 3}


def get_measurement_score(measurement_value, intervals):
    for interval in intervals:
        if measurement_value in interval:
            return intervals[interval]


def check_all_measurements_exist(measurements):
    valid_measurements = {'TEMP', "HR", "RR"}
    received_measurements = set([measurement['type'] for measurement in measurements])
    return True if valid_measurements == received_measurements else False


@app.route('/calculate_news_score', methods=['POST'])
def news_score():
    request_data = request.get_json()
    score = 0
    schema = MeasurementsSchema()
    try:
        # Validate request body against schema data types
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    measurements = result['measurements']
    if not check_all_measurements_exist(measurements):
        return jsonify("Missing measurements"), 400
    for measurement in measurements:
        if measurement['type'] == "TEMP":
            score += get_measurement_score(measurement['value'], temp_intervals)
        if measurement['type'] == "HR":
            score += get_measurement_score(measurement['value'], hr_intervals)
        if measurement['type'] == "RR":
            score += get_measurement_score(measurement['value'], rr_intervals)
    response_body = {
        "score": score
    }

    return response_body


if __name__ == "__main__":
    app.run(port=8000, debug=True)
