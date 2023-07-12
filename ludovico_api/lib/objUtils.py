import json


def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))
