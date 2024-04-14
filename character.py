class Character:
    def __init__(self, health, stamina, attack, defense, skills, mana, level, Character_type, user_name, critical_hit_rate,
                 dodge_rate):
        self.health = health
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.skills = skills
        self.mana = mana
        self.level = level
        self.critical_hit_rate = critical_hit_rate
        self.dodge_rate = dodge_rate
        self.Character_type = Character_type
        self.user_name = user_name
        self.cooldowns = {skill: 0 for skill in skills.keys()}  # create a dict with skill names and remaining cooldown
        # for each skill , number of turns before user can a skill , intitalized to 0.


class Knight(Character):
    def __init__(self):
        user_name = input("Enter your name here :")
        skills = {
            "Heavy strike": {"damage": 4, "level_required": 1, "cooldown": 2},
            "Sword thrust": {"damage": 3, "level_required": 1, "cooldown": 3},
            "Blade of Valor:": {"damage": 6, "level_required": 1, "cooldown": 3},
            "Heavenly Judgement": {"damage": 8, "level_required": 1, "cooldown": 4}}

        super().__init__(health=15, stamina=15, attack=2, defense=16, skills=skills, mana=0, level=1,
                         Character_type="Knight", user_name=user_name,dodge_rate=0.12,critical_hit_rate=0.03)


class Mage(Character):
    def __init__(self):
        user_name = input("Enter your name here :")
        skills = {
            "Fireball": {"damage": 5, "cooldown": 2, "level_required": 1},
            "Ice Shard": {"damage": 4, "cooldown": 3, "level_required": 1},
            "Cry of Thunder": {"damage": 5.5, "cooldown": 3, "level_required": 1},
            "Glimpse of Realization: Emptiness": {"damage": 7, "cooldown": 4, "level_required": 1}
        }
        super().__init__(health=10, stamina=10, attack=3, defense=12, skills=skills, mana=20, level=1,
                         Character_type="Mage", user_name=user_name,dodge_rate=0.05,critical_hit_rate=0.10)


class Murim_Martial_Artist(Character):
    def __init__(self):
        user_name = input("Enter your name here :")
        skills = {
            "Tiger Claw Strike": {"damage": 6, "cooldown": 2, "level_required": 1},
            "Flowing River Dance ": {"damage": 2, "cooldown": 3, "level_required": 2},
            # increase dodge-chance for next attack and counter it , reflect attack by *2
            "Fist of the wind": {"damage": 5.5, "cooldown": 3, "level_required": 1},
            "Dragon's Descent: ": {"damage": 7, "cooldown": 4, "level_required": 1}
        }

        super().__init__(health=50, stamina=10, attack=3, defense=12, skills=skills, mana=20, level=1,
                         Character_type="Mage", user_name=user_name,dodge_rate=0.16,critical_hit_rate=0.50)
# Need to finsh implementing:

# Implement AI states - players vs AI

# AI states : using heuristic/Minmax Algorithm
# Implement cooldown - cooldown refers to number of turns required before skill can be used again
# Implement critical hit rate,dodge chance,defense,Mana consumption
# Implement or remove levels ? - not important right now
