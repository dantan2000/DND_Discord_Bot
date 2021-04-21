DND_Discord_Bot
Created by Dan Tan and Claudia Jodlowski

Technical Specifications
In order to run this project the following must be installed:
    - Add this Discord Bot to any Discord server
        - Discord in Browser: discord.com
        - Discord Bot: https://discord.com/oauth2/authorize?client_id=828358453348925472&scope=bot


To Complete this Project We Used:
    - Python3
    - Installed packages
        - Discord.py
        - Pymongo
        - Pypi
        - DNS Python
    - MongoDBCompass
        - Imported Collections using Json files
        - Read/Write to Tables using Python

Our NoSQL Database Diagram is Under "Updated Model.pdf".
    Collections:
        Abilities: Used to represent abilities or actions gained from a Character's class or race that can then be used in-game.

            - _id: Auto-Generated Id for this Ability
            - name: Name of the Ability
            - description: A brief description of the ability and how player's can use it in-game.

        Characters: Used to represent an individual, fully-created DnD 5e Player Character

            - _id: Auto-Generated Id for this Character
            - user: Discord user associated with this Character
            - name: Name of the Character
            - class: Dnd 5e Class of this Character. Name must be present in Class collection.
            - race: Dnd 5e Race of this Character. Name must be present in Race collection.
            - level: Level of this Character. Must be between 1 and 20.
            - Max Health: The maximum amount of HP this character can have.
            - Current Health: The current amount of HP this character has.
            - Strength: Strength Modifier. Used for Skills, and Attakcs. Must be between 1 and 20.
            - Dexterity: Dexterity Modifer. Used for Skills and Attakcs. Must be between 1 and 20.
            - Constitution: Constitution Modifier. Used for Skills and Attakcs. Must be between 1 and 20.
            - Intelligence: Intelligence Modifer. Used for Skills and Attakcs. Must be between 1 and 20.
            - Wisdom: Wisdom Modifier. Used for Skills and Attakcs. Must be between 1 and 20.
            - Charisma: Charisma Modifier. Used for Skills and Attakcs. Must be between 1 and 20.
            - Proficiencies: An array containing the Weapons, Tools, and Skills this character is proficient in.
            - Abilities: An array containing all class and race abilities this character has.
            - Spell Slots: An array of integers representing the amount of spells this character has remaining
                at each level. The index in the array represents the spell slot level.
            - Gold: The amount of gold this character is carrying.
            - Inventory: A list of items the player is carrying.
            - Equipped Armor: The armor this character is currently wearing.
            - Equipped Weapons: The weapons this character is currently wielding.

        Class: Dnd 5e Classes that represent the abilities and roles a character can fulfill
            - id_: Unique id generated for each object
            - name: Name of the Class
            - description: Brief description contianing the role of each class.
            - hit dice: Interger representing a _ sided die rolled for healing and upgrading max health
            - equipment: Array of Lists of Equipment. Player's choose one option of equipment from each list
                when creating their character
            - saving throws: The skills that this class is proficient in; added to Character's proficiencies.
            - skill options: A list of options the player can choose to be proficient in
            - num skills: The number of skills the player can choose to be proficient in
            - proficiencies: Abilities, Items, and Actions this class in proficient in.
            - level up table: List consisting of embedded level objects
                - proficiency bonus: Bonus that is added to rolls the character is proficient in
                - features: List of abilities gained when a character reaches this level.
            - spellcasting ability (optional): Ability used when rolling for casting spells
            - spell slots table (optional): Array representing the amount of spell slots available at each level.
                Only used in spellcasting classes.
        
        Item: Represents any armor, weapons, and equipment characters can carry in their inventory
            - _id: Unique id generated for each object.
            - name: Name of the item.
            - description: Brief description of the item and its properties.
            - type: Either Armor, Weapon, or Equipment
            - weapon:
                - weapontype: Either simple or martial
                - damage: 
                    - amount: description of the amount and type of dice to roll
                    - type: the type of damage being dealt.
                - properties: Properties of a weapon that determine how it can be used in combat
            - armor:
                - armortype: Type of armor by weight. Eitehr light, medium, heavy, or a shield.
                - armor class: The amount of protection this armor gives to the character when worn.
            -equipment:                

        Race:
            - _id: Unique id generated for each object.
            - name: Name of the race.
            - description: Brief description containing the characteristics of each race.
            - size: Size of the race. Used for certain spell and weapon effects.
            - speed: How quickly this race can move per turn.
            - Strength: How many points to add to the character's base Strength ability.
            - Dexterity: How many points to add to the character's base Dexterity ability.
            - Constitution: How many points to add to the character's base Constitution ability.
            - Intelligence: How many points to add to the character's base Intelligence ability.
            - Wisdom: How many points to add to the character's base Wisdom ability.
            - Charisma: How many points to add to the character's base Charisma.
            - Abilties: Abilities a character gains from being this race.

        Skills: Used to roll for specific actions a player wants to take. Each uses one of the six core abilities as a modifer.
            - _id: Unique id generated for each object.
            - name: Name of the skill.
            - type: Which one of the six core abilities this skill uses as a modifier/

        Spells: Represents spells that characters can cast
            - _id: Unique id generated for each object.
            - name: Name of the spell.
            - Casting time: How long it takes to cast this spell.
            - Range: How far this spell can reach.
            - Description: Description of properties and effects of the spell.
            - is cantrip: Describes whether or not this spell is a cantrip
            - damage (optional): 
                - amount: description of the amount and type of dice to roll
                - type: the type of damage being dealt.
            - minimum level (optional): The minimum level this spell can be cast at.


        
            


    
