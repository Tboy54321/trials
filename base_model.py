import json
import datetime
import uuid
from models.engine.file_storage import FileStorage
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
        storage.save()
    # def update(self, **kwargs):
    #     """Update instance attributes with new values."""
    #     for key, value in kwargs.items():
    #         setattr(self, key, value)
    #     self.updated_at = datetime.now()

    # def update(self, name=None, email=None, password=None):
    #     # A GENERAL METHOD
    #     if name:
    #         self.name = name
    #     if email:
    #         self.email = email
    #     if password:
    #         self.password = password
    #     self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_data = self.__dict__.copy()
        # if "created_at" in dict_data:
        dict_data["created_at"] = self.created_at.isoformat()
        # if "updated_at" in dict_data:
        dict_data["updated_at"] = self.updated_at.isoformat()
        dict_data["__class__"] = self.__class__.__name__
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
        print(f'[{type(self).__name__}] ({self.id}) <{self.__dict__}>')

    # def to_dict(self):
    #     data = {
    #         'users': [user.__dict__ for user in users],
    #         'cities': [city.__dict__ for city in cities],
    #         'places': [place.__dict__ for place in places]
    #     }
    #     with open("../database.json", "w") as file:
    #         json.dump(data, file, indent=2)
    # @property
    # def user(self):
    #     return self.__user__
    #
    # @user.setter
    # def user(self, user_content):
    #     return self.__user = user_content
    # def save_to_file(self):
    #     content = {key: }
    #     with open('../storage/database.json', 'w') as file:
    #         content = json.dumps(self.user)
    #         file.write(content)

