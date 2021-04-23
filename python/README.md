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

    
User Flow:
    When users first put this discord bot within their discord server. There will be a few commands available by default, but
    many will begin using this discord bot by creating their DnD character. This will be done with the $createCharacter command.
        - $createCharacter Name
    This creates the template for a player character. Users can then call a series of functions that allow them to set the values of their characters. Discord's Bot API does not allow for a traditional stdout, wait and check for user stdin input, which is why users must all these methods individually. However before a character is pushed to the database, it will check whether a character has all necessary fields and is complete, and will notify the user which fields they must fill out.
    The following functions must be called in order to create a full and complete character:

        - $setLevel(level): Sets the open character's level to the given level.
        - $setStr(score): Set's the character's Strength score.
        - $setDex(score): Set's the character's Dexterity score.
        - $setCon(score): Set's the character's Constitution score.
        - $setInt(score): Set's the character's Intelligence score.
        - $setWis(score): Set's the character's Wisdom score.
        - $setCha(score): Set's the character's Charisma score.
        - $setMaxHP(hp): Set's the character's maximum health.
        - $setRace(race): Set's the character's race. Race must be present in race collection.
        - $setClass(ctx, className): Set's the character's class. Class must be present in class collection.
        - $addMaxHP(hp): Add's the given value to the character's maximum health.
        - $addAbilityFeature(*args): Adds the given ability to the character's abilities.
            -can be called as $addAbility and $addFeature
        - $addProficiency(*args): Adds the given proficiency to the character's proficiencies.
        - $takeDmg(hp): Removes the given amount from the character's current HP.
        - $heal(hp): Adds the given amount from the character's current HP.
        - $addItem(*args): Adds the given item into the character's inventory.
        - $removeItem(*args): Removes the given item from the character's inventory
        - $addGold(qty): Gives the amount of gold to the character.
        - $removeGold(qty): Removes the amount of gold from the character.
        - $don(*args): Equips the given armor.
        - $doff(*args): Unequips the given armor.
        - $isComplete(): Checks whether the character is complete, valid, and ready to be added or updated in the database.
        - $dumpCharacter(): Prints all information about the open character.

    Once a player's character is complete the user can call the $save and $close commands to save their changes and save the new character to the database. If they wish to use the character again, they can call $open(charactername). Each user can only have one character active at a time. Users can also call $deleteCharacter(charactername) if they wish to remove their character from the database. 

    The discord bot also contains a $roll command. When a user does not have a character open, they can use the $roll in the following format:
        $roll 1d20 + x
    where the number before "d" indicates the number of dice to roll, and the number after indicates the number of sides on the dice. Any integer x can also be added to the roll. If a player has a character currently open, they can also use the roll command to roll any skills present in DnD 5e. For example:
        $roll Int
        $roll Animal Handling


Future Work
    Our current planned uses of the database is to help people that are running Dungeons and Dragons campaigns through discord servers. The database would be able to store information on player character's, and give descriptions for available Classes, Races, Abilities, Spells, Weapons, Armor, and other Items. Our goal is to make playing a DnD online an easier experience by integrating parts of the Tabletop RPG right into the server, instead of having users use third party websites and discord at the same time. The main use will be to have users keep track of any characters they have created. 
        
    There are many areas for added functionality. Right now, much of the character creation process relies on players still having knowledge of the rules of the game. There should be options in character creation so that player's can choose which rulesets they wish to follow, whether it be the standard character creation rulset or a customized one. This would help lower the difficulty of entry for users, as they may not know all of the rules for setting character abilities, health, and proficiencies. 

    As Dungeons and Dragons is an incredibly expansive game, one goal would be to at least include all Standard Classes, Races, Spells, and Items that are in the original Player's Handbook that would allow for full functionality of the standard rules of Dungeon and Dragons 5th edition. While it would be exciting to include all extra content provided by Wizards of the Coast, this goal would be very difficult to obtain in a reasonable amount of time. It would also be wonderful to battle functionality, allowing player's to roll Initiative, Attack Enemies, Cast Spells, and take other actions during combat. This would limit the amount of calculations user's would have to do, and create a smoother user experience. Of course, battles in Dungeon and Dragons are one of the aspects that allow for player creativity and "bending the rules" to some the degree, so it would be impoosible to create a completely functional implementation for each dnd party.

    It might also be useful to create Dungeon Master specific commands, which could be given to the admin user on the server. This added functionality could lead to a Planned/Saved Battles collection, where Dungeon Master's could keep track of planned enemy encounters. A consequence of this would also be the creation of an Enemy Collection, where information on all of the various monsters players can fight would be stored.

    In short, Dungeons and Dragons is a very expansive game, which means our Discord bot and databases also have the potential to be greatly expanded upon.