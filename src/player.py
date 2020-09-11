# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, bag = []):
        self.name = name
        self.current_room = current_room
        self.bag = bag
    def __str__(self):
        return f'{self.name} has {self.bag} in {self.current_room}'
    def addItem(self, item):
        if len(self.bag) < 3:
            self.bag.append(item)
        else:
            print('You have too many items!\n')
    def dropItem(self, index):
        if len(self.bag) > 0:
            self.bag.remove(self.bag[index-1])