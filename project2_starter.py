"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Xavier Rothwell
Date: 11/10/25
AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength #sets the Characters variables 
        self.magic = magic
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        pass
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength #this allows it to print the amount of damage that was delt and also makes a damage variable out of the strength one made previously
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage
        pass
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        if self.health - damage > 0:
            self.health -= damage #makes sure that once the characters health gets depleted to less than zero it will be set to zero
        else:
            self.health = 0
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        pass
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print("=== Current Stats ===")
        print(f"Name: {self.name}")
        print(f"Strength: {self.strength}") #Just prints the current stats/variables that we have set in place 
        print(f"Magic: {self.magic}")
        print(f"Health: {self.health}")
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        pass

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class  # calls back to the begining where we set the character's variables then makes 3 new ones 
        self.level = 1
        self.experience = 0
        # TODO: Call super().__init__() with the basic character info
        # TODO: Store the character_class (like "Warrior", "Mage", etc.)
        # TODO: Add any other player-specific attributes (level, experience, etc.)
        pass
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        super.display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}") #calls the other print of data  the adds the new variables print statments to it 
        print(f"Experience Points: {self.experience}")
        # TODO: Call the parent's display_stats method using super()
        # TODO: Then print additional player info like class and level
        pass

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, "Warrior", 120, 15, 5) # calls back to the name variable and adds The title of the class and its other stats that will go with it
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        damage = self.strength + 5 #changes the total amount of damage being dealt to plus 5 the normal rate
        print(f"{self.name} slashes powerfully for {damage} damage!")
        target.take_damage(damage)
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        pass
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        damage = self.strength * 2 #this changes the damage being dealt to be two times as strong as the regular damage but is a special ability only for warrior class
        print(f" {self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        pass

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        super().__init__(name, "Mage", 80, 8, 20) # calls to the name and Enters in the data titling it mage also adding in the stats for the mage class 
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        damage = self.magic + 5 #Almost the exact same thing as the strength damage boost section but just with magic as the variable being used
        print(f"{self.name} lauches Magic Bolt for {damage} damage!")
        target.take_damage(damage)
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        pass
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        damage = self.magic + 20  # same as the speical attack for the warrior class just this one is only for the Mage class
        target.take_damage(damage) # to make it different I changed the amount of speical damage to make each class more unique 
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        pass

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        super().__init__(name, "Rogue", 90, 12, 10) # calls back to the name variable and sets it to Rogue then adds the stats that go with that new class
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # AI was used for the Logical parts of this code
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage = self.strength + 20
            print(f" CRITICAL HIT! {self.name} strikes {target.name} for {damage} damage!")
        else: # but with all this code it just means with every attack there will be a dice rolled and if the number it lands on is less than or equal to 3 it will impliment that bonus damage 
            damage = self.strength
            print(f"{self.name} swiftly attacks for {damage} damage.")
        target.take_damage(damage)
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        pass
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        damage = self.strength + 15
        target.takedamage(damage) #using this ability will allow a sure hit with the increased damaged 
        # TODO: Implement sneak attack
        # Should always do critical damage
        pass

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name # like it says to do i created a weapon then will set the name of the weapon created later in the code also giving the weapon a damage bonus when used 
        self.damage_bonus = damage_bonus
        # TODO: Store weapon name and damage bonus
        pass
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        print("==== Weapon Details ===")
        print(f"Weapon: {self.name}")
        print(f"Bonus Damage: {self.damage_bonus}")
        # TODO: Print weapon name and damage bonus
        pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")

    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health

    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0) 
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health

    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)

    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()

    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()

    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
