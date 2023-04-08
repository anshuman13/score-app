from marshmallow import Schema, fields

from serializers.MeasurementSerializer import TypeField, ValueField


class NewsScoreSchema(Schema):
    type = TypeField(required=True)
    value = ValueField(required=True)


class MeasurementsSchema(Schema):
    measurements = fields.List(fields.Nested(NewsScoreSchema), required=True)
