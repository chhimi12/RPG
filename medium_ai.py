import random
from character import Character, Knight, Mage, Murim_Martial_Artist
from easy_ai import AI_Agent


class Medium_AI_Agent(AI_Agent):  # Inherit from AI_Agent

    @classmethod
    def use_skill(cls, user_character):
        print("Medium AI playing ")
        available_skills = {move: info for move, info in user_character.skills.items() if
                            info["level_required"] <= user_character.level and user_character.cooldowns[move] == 0}

        if available_skills:
            # Strategies:

            # 1. Prefer high-damage skills
            highest_damage = max(info['damage'] for info in available_skills.values())
            skills_by_damage = [(skill, info) for skill, info in available_skills.items() if info['damage'] == highest_damage]
            skill_name, skill_info = random.choice(skills_by_damage)

            # # 2. Save powerful skills if enemy is low
            # if user_character.health / user_character.health >= 0.5:
            #     highest_cooldown = max(info['cooldown'] for info in available_skills.values())
            #     skills_by_cooldown = [skill for skill, info in available_skills.items() if info['cooldown'] == highest_cooldown]
            #     if skills_by_cooldown:
            #         skill_name = random.choice(skills_by_cooldown)

            damage = skill_info['damage']
            user_character.cooldowns[skill_name] = skill_info['cooldown']
            print(f"{user_character.user_name} used {skill_name} and caused {damage} damage")
            return damage
        else:
            return user_character.attack  # Fallback to basic attack