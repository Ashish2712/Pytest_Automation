"""
This module contains class related to stack to understand how pytest works with it
"""


# ------------------
# class: Stack
# ------------------


class Stack:

    def __init__(self):
        self.box = []

    def add(self, data):
        if str(type(data)) ==str(list):
            return self.box.extend(data)
        else:
            return self.box.append(data)
        

    def remove(self, value):
        for i in self.box:
            if i == value:
                return self.box.remove(value)

    def length(self):
        count = 0
        for i in self.box:
            count += 1
        return count


    

