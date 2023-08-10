#!/usr/bin/python3
import json
import datetime
import uuid
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs:
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.datetime.strftime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()
        print("I am saved")
        storage.save()

    def to_dict(self):
        dict_data = self.__dict__.copy()
        if "created_at" in dict_data:
            dict_data["created_at"] = self.created_at.isoformat()
        if "updated_at" in dict_data:
            dict_data["updated_at"] = self.updated_at.isoformat()
        dict_data["__class__"] = type(self).__name__
        return dict_data

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls.from_dict(data)

    def delete(self):
        #  GENERAL METHOD
        pass

    def __str__(self):
        return (f'[{type(self).__name__}] ({self.id}) <{self.__dict__}>')
