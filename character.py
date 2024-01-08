class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        """initialise a charater with a name with char_name and description with char_description"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    
    # Describe this character
    def describe(self):
        """name and describe the character"""
        print( self.name + " is here!" )
        print( self.description )

    def get_name(self):
        """returns character name"""
        return self.name
        
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """ sets characters conversation with conversation"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """use to talk to the character"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you either")

    # Fight with this character
    def fight(self, combat_item):
        """use to fight character with combat_item"""
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    enemies_defeated = 0
    
    def __init__(self, char_name, char_description): #create a constructor
        """Initialise an emeny character"""
        super().__init__(char_name, char_description) # to make an enemry first make a Character object and then we'll customise it
        self.weakness = None

    def fight(self, combat_item):
        """use to fight enemy with combat_item"""
        if combat_item == self.weakness:
            print("You defeated " + self.name + " off with " + combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " is not effected by " + combat_item)
            print(self.name + " has injured you.")
            return False
        
    def set_weakness(self, item_weakness):
        """set enemy weakness with item_weakness"""
        self.weakness = item_weakness
        
    def get_weakness(self):
        """return weakness"""
        return self.weakness

    def set_enemies_defeated(self, num_defeated):
        """use to set number of enemies defeated"""
        Enemy.enemies_defeated = num_defeated
        
    def get_enemies_defeated(self):
        """ return number of enemies defeated"""
        return Enemy.enemies_defeated
    
class Friend(Character):
    
    def __init__(self, char_name, char_description): #create a constructor
        """initialise friendly character"""
        super().__init__(char_name, char_description) # to make an enemry first make a Character object and then we'll customise it
        self.feeling = None

    def hug(self):
        """friend hugs"""
        print(self.name + " hugs you back.")

