class Character:
    def __init__(self, health, attack, defense, skills, mana, level, Character_type, user_name,
                 critical_hit_rate,
                 dodge_rate):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.skills = skills
        self.mana = mana
        self.level = level
        self.critical_hit_rate = critical_hit_rate
        self.dodge_rate = dodge_rate
        self.Character_type = Character_type
        self.user_name = user_name
        self.cooldowns = {skill: 0 for skill in skills.keys()}


#          create a dictionary where the keys are obtained from skills.keys() and each value is given cooldown = 0

class Knight(Character):
    def __init__(self, is_ai=False):

        if is_ai == False:
            user_name = input("Enter your name here :")
        else:
            user_name = "Arthur"

        skills = {
            "Heavy strike": {"damage": 4, "level_required": 1, "cooldown": 2},
            "Sword thrust": {"damage": 3, "level_required": 1, "cooldown": 3},
            "Blade of Valor": {"damage": 6, "level_required": 1, "cooldown": 3},
            "Heavenly Judgement": {"damage": 8, "level_required": 1, "cooldown": 4},}

        super().__init__(health=15, attack=4, defense=16, skills=skills, mana=0, level=1,
                         Character_type="Knight", user_name=user_name, dodge_rate=0.12, critical_hit_rate=0.03)


class Mage(Character):
    def __init__(self, is_ai=False):
        if is_ai == False:
            user_name = input("Enter your name here :")
        else:
            user_name = "Arc"
        skills = {

            "Buff_skills":{
                "Basic Heal": {"Cooldown": 5,"Buff Type":"Health Buff","Duration":1,"Amount":1.5,"Counter":0}
            },

            "attack_skills": {
                "Fireball": {"damage": 5, "cooldown": 2, "level_required": 1},
                "Ice Shard": {"damage": 4, "cooldown": 3, "level_required": 1},
                "Cry of Thunder": {"damage": 5.5, "cooldown": 3, "level_required": 1},
                "Glimpse of Realization: Emptiness": {"damage": 7, "cooldown": 4, "level_required": 1}
            }
        }
        super().__init__(health=10, attack=2, defense=12, skills=skills, mana=20, level=1,
                         Character_type="Mage", user_name=user_name, dodge_rate=0.18
                         , critical_hit_rate=0.10)


class Murim_Martial_Artist(Character):
    def __init__(self, is_ai=False):
        if is_ai == False:
            user_name = input("Enter your name here :")
        else:
            user_name = "Drogyom"

        skills = {
            "Tiger Claw Strike": {"damage": 6, "cooldown": 2, "level_required": 1},
            "Flowing River Dance": {"damage": 2, "cooldown": 3, "level_required": 1},
            # increase dodge-chance for next attack and counter it , reflect attack by *2
            "Fist of the wind": {"damage": 5.5, "cooldown": 3, "level_required": 1},
            "Dragon's Descent": {"damage": 7, "cooldown": 4, "level_required": 1}
        }

        super().__init__(health=16, attack=4, defense=12, skills=skills, mana=20, level=1,
                         Character_type="Mage", user_name=user_name, dodge_rate=0.12, critical_hit_rate=0.09)

# Need to finsh implementing:
# Implement AI states - players vs AI

# AI states : using heuristic/Minmax Algorithm
# Implement cooldown - cooldown refers to number of turns required before skill can be used again
# Implement critical hit rate,dodge chance,defense,Mana consumption
# Implement or remove levels ? - not important right now
