import random
from character import Character, Knight, Mage, Murim_Martial_Artist


class AI_Agent:
    @classmethod
    def choose_character(cls):
        character_types = ["Knight", "Mage", "Murim_Martial_Artist"]
        chosen_character = random.choice(character_types)

        if chosen_character == "Knight":
            character = Knight()
            print('AI has chosen the valiant Knight!')
            print(
                'With valor as their blade and honor as their shield, the knight embarks on a noble quest, carving their legend across the realms')
        elif chosen_character == "Mage":
            character = Mage()
            print('AI has chosen the mystical Mage!')
            print(
                "Casting spells with a flick of their wrist, the mage weaves intricate arcane energies to shape the very fabric of reality")
        elif chosen_character == "Murim_Martial_Artist":
            character = Murim_Martial_Artist()
            print('AI has chosen the disciplined Murim Martial Artist!')
            print("The Murim Artist wields chi with precision, sculpting combat into a seamless display of mastery.")

        return character

    @classmethod
    def use_skill(cls, user_character):

        available_skills = {move: info for move, info in user_character.skills.items() if
                            info["level_required"] <= user_character.level and user_character.cooldowns[move] == 0}
        # move and ifno are initalized as dict pairs, then we iterate over key,value pair in character skills. both move and info will store each skills and its info
        # move is the name of the skill which is passed into cooldowns to check remaining cool down for the move.

        if available_skills:
            skill_name = random.choice(list(available_skills.keys()))
            damage = available_skills[skill_name]['damage']
            user_character.cooldowns[skill_name] = user_character.skills[skill_name]['cooldown']
            print(f"{user_character.user_name} used {skill_name} and caused {damage} damage")
            return damage
        else:
            return user_character.attack
