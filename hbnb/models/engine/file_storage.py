#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = '../../file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        
        FileStorage.__objects[key] = obj

    def save(self):
        serialized = {}
        '''
        with open(self.__file_path, 'w') as content:
            data = {key:obj.to_dict() for (key, obj) in self.__objects.items()}
            json.dump(data, content)
        '''
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        
        with open(self.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as content:
                file = json.load(content)
                for key, value in file.items():
                    class_, obj_id = key.split(".")
                    cls = eval(class_)
                    obj = cls(**value)
                    self.new(obj)
