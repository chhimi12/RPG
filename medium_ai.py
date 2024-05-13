import random
from character import Character, Knight, Mage, Murim_Martial_Artist
from easy_ai import AI_Agent
from easy_ai import AI_Agent

class Medium_AI_Agent():

    @classmethod
    def choose_character(cls):
        character_types = ["Knight", "Mage", "Murim_Martial_Artist"]
        chosen_character = random.choice(character_types)
        chosen_character = "Mage"

        if chosen_character == "Knight":
            character = Knight(is_ai=True)
            print(f'{character.user_name} has chosen the valiant Knight!')
            print(
                'With valor as their blade and honor as their shield, the knight embarks on a noble quest, carving their legend across the realms')
        elif chosen_character == "Mage":
            character = Mage(is_ai=True)
            print('AI has chosen the mystical Mage!')
            print(
                "Casting spells with a flick of their wrist, the mage weaves intricate arcane energies to shape the very fabric of reality")
        elif chosen_character == "Murim_Martial_Artist":
            character = Murim_Martial_Artist(is_ai=True)
            print('AI has chosen the disciplined Murim Martial Artist!')
            print("The Murim Artist wields chi with precision, sculpting combat into a seamless display of mastery.")

        return character


    @classmethod
    def use_skill(cls, user_character):
        print("Medium AI playing ")
        available_skills = {move: info for move, info in user_character.skills.items() if
                            info["level_required"] <= user_character.level and user_character.cooldowns[move] == 0}

        if available_skills:
            highest_damage = max(info['damage'] for info in available_skills.values())
            skills_by_damage = [(skill, info) for skill, info in available_skills.items() if info['damage'] == highest_damage]
            skill_name, skill_info = random.choice(skills_by_damage)

            damage = skill_info['damage']
            user_character.cooldowns[skill_name] = skill_info['cooldown']
            # once a skill is used it will obtain a cool down value
            print(f"{user_character.user_name} used {skill_name} and caused {damage} damage")
            return damage
        else:
            return user_character.attack  # Fallback to basic attack