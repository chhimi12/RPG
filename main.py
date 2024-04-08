import character
from character import Knight, Mage


class Game:

    def start(self, player_1, player_2):

        while True:  # both players are alive
            print(f"{player_1.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_1)
            player_2.health -= Attack
            if player_2.health <= 0:
                print(f"{player_2.user_name} has been slain!")
                return 0

            print(f"{player_2.user_name}'s Health:{player_2.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"{player_2.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_2) # player two uses their skill
            player_1.health -= Attack
            if player_1.health <= 0:
                print(f"{player_1.user_name} has been slain!")
                return 0

            print(f"{player_1.user_name}'s Health:{player_1.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    def choose_character(self):
        character_types = ["Knight", "Mage"]
        print("Select your character type:")
        for i, character_type in enumerate(character_types, start=1):
            print(f"{i}. {character_type}")

        choice = int(input("Enter the number of your choice: "))
        if choice < 1 or choice > len(character_types):
            print("Invalid choice. Please select a valid option.")
            return self.choose_character()  # ask user to enter again

        character_type = character_types[choice - 1]
        if character_type == "Knight":
            print(
                'With valor as their blade and honor as their shield, the knight embarks on a noble quest, carving their legend across the realms')
            return Knight()  # create a knight object here

        if character_type == "Mage":
            print(
                "Casting spells with a flick of their wrist, the mage weaves intricate arcane energies to shape the very fabric of reality")
            return Mage()  # create a knight object here

    def use_skill(self, user_character):

        choice = int(input("Enter 1 for Basic attack and 2 to view skills: "))
        if choice == 1:
            print(f"You used a basic attack and caused {user_character.attack} damage")
            return user_character.attack
        if choice == 2:

            available_skills = {move: info for move, info in user_character.skills.items() if
                                info[
                                    "level_required"] <= user_character.level}  # python dict where we filter out skills by
            print("Available skills:")
            for i, skill in enumerate(available_skills.keys(), start=1):
                print(f"{i}. {skill}")

            choice = int(input("Enter the Index of the skill you want to use: "))
            skill_name = list(available_skills.keys())[choice - 1]
            print(f"You used {skill_name} and caused {available_skills[skill_name]['damage']} damage")
            return available_skills[skill_name]['damage']


game = Game()
player_1 = game.choose_character()
player_2 = game.choose_character()
game.start(player_1, player_2)
