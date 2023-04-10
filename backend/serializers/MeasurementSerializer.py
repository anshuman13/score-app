from marshmallow import fields, ValidationError


class TypeField(fields.Field):
    """Field that serializes and checks for valid score type
    """

    def _serialize(self, value, attr, obj, **kwargs):
        return value

    def _deserialize(self, value, attr, data, **kwargs):
        if attr == 'type' and value in ["TEMP", "RR", "HR"]:
            return value
        else:
            raise ValidationError("Invalid Type")


class ValueField(fields.Field):
    """Field that serializes and checks for valid values for measurements
    """

    def _serialize(self, value, attr, obj, **kwargs):
        return value

    def _deserialize(self, value, attr, data, **kwargs):
        if attr == 'value' and not isinstance(value, float) and not isinstance(value,
                                                                               int):
            raise ValidationError("Value must contain only digits")
        elif attr == 'value' and data['type'] == "TEMP" and not (31 < value <= 42):
            raise ValidationError("Body temperature is out of range")
        elif attr == 'value' and data['type'] == "HR" and not (25 < value <= 220):
            raise ValidationError("Heart rate is out of range")
        elif attr == 'value' and data['type'] == "RR" and not (3 < value <= 60):
            raise ValidationError("Respiratory rate is out of range")
        else:
            return value
