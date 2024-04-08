import pygame

class Character:
    def __init__(self, x, y, width, height, health, stamina, attack, defense, skills, mana, level, Character_type, user_name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.skills = skills
        self.mana = mana
        self.level = level
        self.Character_type = Character_type
        self.user_name = user_name

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

class Knight(Character):
    def __init__(self):
        user_name = input("Enter your name here :")
        skills = {
            "Heavy strike": {"damage": 4, "level_required": 1},
            "Sword thrust": {"damage": 3, "level_required": 1},
            "Blade of Valor:": {"damage": 6, "level_required": 3},
            "Heavenly Judgement": {"damage": 8, "level_required": 5}}

        super().__init__(x=100, y=100, width=50, height=50, health=15, stamina=15, attack=2, defense=16, skills=skills, mana=0, level=1, Character_type="Knight", user_name=user_name)

class Mage(Character):
    def __init__(self):
        user_name = input("Enter your name here :")
        skills = {
            "Fireball": {"damage": 5, "cooldown": 2, "level_required": 1},
            "Ice Shard": {"damage": 4, "cooldown": 3, "level_required": 3},
            "Glimpse of Realization: Thunderbolt": {"damage": 7, "cooldown": 4, "level_required": 5}
        }

        super().__init__(x=100, y=100, width=50, height=50, health=10, stamina=10, attack=3, defense=12, skills=skills, mana=10, level=1, Character_type="Mage", user_name=user_name)