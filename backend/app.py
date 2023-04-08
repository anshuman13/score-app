from flask import Flask, request, jsonify
from flask_cors import CORS
from marshmallow import ValidationError
from constants import temp_intervals, rr_intervals, hr_intervals
from schema.MeasurementSchema import MeasurementsSchema

app = Flask(__name__)
CORS(app)


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
