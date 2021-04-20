import DB
import Character


character = DB.openCharacter("axel axeman")
character.c_str = 20 - character.c_str 
character.c_dex = 20 - character.c_dex 
character.c_con = 20 - character.c_con 
character.c_int = 20 - character.c_int 
character.c_wis = 20 - character.c_wis 
character.c_cha = 20 - character.c_cha 
print(character)

DB.saveCharacter(character)