class Room():

    def __init__(self, room_name):
        """initialise rooms with room_name"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
    def set_character(self, new_character):
        """set new character in the room"""
        self.character = new_character

    def get_character(self):
        """ return character in the room"""
        return self.character

    def set_item(self, new_item):
        """ set an item in the room"""
        self.item = new_item

    def get_item(self):
        """ return the item in the room"""
        return self.item
        
    def set_description(self, room_description):
        """use to set room description"""
        self.description = room_description

    def get_description(self):
        """return the room description"""
        return self.description

    def set_name(self, room_name):
        """set the room name"""
        self.name = room_name
        
    def get_name(self):
        """return the room name"""
        return self.name 

    def describe(self):
        """use to print description of room"""
        print( self.description )

    def link_room(self, room_to_link, direction):
        """use to link rooms together with a direction eg. north, south etc."""
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        """return the details of the room you are currently in"""
        print("You are in the " + self.get_name())
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        

    def move(self, direction):
        """use to move between rooms"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    
