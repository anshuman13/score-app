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
        if attr == 'value' and not isinstance(value, int):
            raise ValidationError("Value must contain only digits")
        elif attr == 'value' and data['type'] == "TEMP" and value not in range(32, 43):
            raise ValidationError("Body temperature is out of range")
        elif attr == 'value' and data['type'] == "HR" and value not in range(26, 221):
            raise ValidationError("Heart rate is out of range")
        elif attr == 'value' and data['type'] == "RR" and value not in range(4, 60):
            raise ValidationError("Respiratory rate is out of range")
        else:
            return value
