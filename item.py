class Item():

    def __init__(self, item_name):
        """initialise items"""
        self.name = item_name
        self.description = None
        self.room_location = {}

    def set_description(self, item_description):
        """use to set item description"""
        self.description = item_description

    def get_description(self):
        """returns item description"""
        return self.description

    def set_name(self, item_name):
        """sets the name of the item to item_name"""
        self.name = item_name

    def get_name(self):
        """returns the item name"""
        return self.name

    def describe(self):
        """prints out item description"""
        print( self.description )

    def room_loc(self, item_in_room, item):
        """set the location of the item"""
        self.room_location[item] = item_in_room
        
    def get_details(self):
        """prints details of room location with item """
        print("You are in " + self.room_location)
        for item in self.room_location:
            room = self.room_location[item]
            print("Do you want to look for the" + item + " in the " + room.get_name()) 

    def look(self, item):
        """use to look for item in room"""
        if item in self.room_location:
            print("you found item")
            return self.room_location[item]
        else:
            print("item not in room ")
            return self
