#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    instances = {}
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        try:
            """
            if class_ == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
            """
            model_class = globals()[class_name]
            print(model_class)
            new_instance = model_class()
            new_instance.save()
            print(new_instance.id)
        # except ImportError:
        except KeyError:
            print("** class doesn't exist **")


    def do_show(self, line):
        
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if len(args) < 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = None

        if len(args) > 1:
            instance_id = args[1]

        try:
            model_class = globals()[class_name]
            instance = self.instances.get(instance_id)

            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line):

        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        instance_id = None

        #if len(args) < 1:
            #print("** instance id missing **")
            #return

        if len(args) > 1:
            instance_id = args[1]
            
        if instance_id == "":
            print("instance id missing")
            return

        try:
            model_class = globals()[class_name]
            instance = self.instances.get(instance_id)

            if instance:
                del self.instances[instance_id]
                instance.save()

            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
