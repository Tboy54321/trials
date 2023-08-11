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

        '''
    def save(self):
        serialized = {}
        
        with open(self.__file_path, 'w') as content:
            data = {key:obj.to_dict() for (key, obj) in self.__objects.items()}
            json.dump(data, content)
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        
        with open(self.__file_path, "a") as f:
            json.dump(serialized, f, indent=4)
        '''
    def save(self):
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        existing_data = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)

        existing_data.update(obj_dict)

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=4)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as content:
                file = json.load(content)
                
                for key, value in file.items():
                    class_, obj_id = key.split(".")
                    cls = globals().get(class_)
                    if cls:
                        obj = cls(**value)
                        FileStorage.new(obj)
                FileStorage.__objects = file
