import random

import character
from character import Knight, Mage
import easy_ai
from easy_ai import AI_Agent
from medium_ai import Medium_AI_Agent


class Game:

    def criticial(self, attacker, defender, damage):
        """Handles critical hits and dodging, modifying damage if applicable.

            Args:
                attacker (Character): The character performing the attack.
                defender (Character): The character being attacked.
                damage (int): The base damage amount.

            Returns:
                bool: True if the attack hit, False if it was dodged.
            """

        if random.random() < defender.dodge_rate:
            print(f"{defender.user_name} dodged the attack!")
            return False  # Attack missed

        if random.random() < attacker.critical_hit_rate:
            damage *= 2
            print(f"{attacker.user_name} landed a critical hit!")

        print(f"{attacker.user_name} dealt {damage} damage to {defender.user_name}!")
        return True  # Attack hit

    def start_against_AI(self, player_1, ai):
        while True:  # both players are alive
            print(f"{player_1.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_1)  # player 1 uses skill
            if self.criticial(player_1, ai, Attack):  # check if the attack will result in a critical hit
                ai.health -= Attack
            if ai.health <= 0:
                print(f"{ai.user_name} has been slain!")
                return 0

            print(f"{ai.user_name}'s Health:{ai.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"{ai.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = AI_Agent.use_skill(ai)  # ai uses skill
            if self.criticial(ai, player_1, Attack):
                player_1.health -= Attack

            if player_1.health <= 0:
                print(f"{player_1.user_name} has been slain!")
                return 0

            print(f"{player_1.user_name}'s Health:{player_1.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

            # Decrement cooldowns
            for skill in player_1.cooldowns.keys():
                if player_1.cooldowns[skill] > 0:
                    player_1.cooldowns[skill] -= 1
            for skill in ai.cooldowns.keys():
                if ai.cooldowns[skill] > 0:
                    ai.cooldowns[skill] -= 1

    def start(self, player_1, player_2):

        while True:  # both players are alive
            print(f"{player_1.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_1)  # player 1 attack player 2
            if self.criticial(player_1, player_2, Attack):
                player_2.health -= Attack
            if player_2.health <= 0:
                print(f"{player_2.user_name} has been slain!")
                return 0

            print(f"{player_2.user_name}'s Health:{player_2.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"{player_2.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_2)  # player 2 attacks player 1
            if self.criticial(player_1, player_2, Attack):
                player_2.health -= Attack

            if player_1.health <= 0:
                print(f"{player_1.user_name} has been slain!")
                return 0

            print(f"{player_1.user_name}'s Health:{player_1.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

            # Decrement cooldowns
            for skill in player_1.cooldowns.keys():
                if player_1.cooldowns[skill] > 0:
                    player_1.cooldowns[skill] -= 1
            for skill in player_2.cooldowns.keys():
                if player_2.cooldowns[skill] > 0:
                    player_2.cooldowns[skill] -= 1

    def choose_character(self):
        while True:
            try:
                print(" - - - - - - - - - - - - - -- - - - - - -- - - - - - -- - - - - - - \n")

                character_types = ["Knight", "Mage", "Murim_Martial_Artist"]
                print("Select your character type:")
                for i, character_type in enumerate(character_types, start=1):
                    print(f"{i}. {character_type}")

                choice = int(input("Enter the number of your choice : "))
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

                if character_type == "Murim_Martial_Artist":
                    print(
                        "The Murim Artist wields chi with precision, sculpting combat into a seamless display of mastery.")
                    return character.Murim_Martial_Artist()  # create a knight object here
            except ValueError:
                print("Invalid input. Please enter a number.")

    def use_skill(self, user_character):
        while True:
            try:
                choice = int(input("Enter 1 for Basic attack and 2 to view skills : "))

                if choice == 1:
                    print(f"You used a basic attack and caused {user_character.attack} damage")
                    return user_character.attack
                if choice == 2:

                    available_skills = {move: info for move, info in user_character.skills.items() if
                                        info[
                                            "level_required"] <= user_character.level}
                    # move and ifno are initalized as dict pairs, then we iterate over key,value pair in character skills. both move and info will store each skills and its info
                    print("Available skills:")
                    for i, skill in enumerate(available_skills.keys(), start=1):
                        print(f"{i}. {skill}")

                    choice = int(input("Enter the Index of the skill you want to use or 0 to go back: "))
                    if choice == 0:
                        continue
                    skill_name = list(available_skills.keys())[choice - 1]
                    if user_character.cooldowns[skill_name] > 0:  # new line, at first its initalized to 0
                        print(f"{skill_name} is still on cooldown for {user_character.cooldowns[skill_name]} turns.")
                    else:

                        damage = available_skills[skill_name]['damage']
                        print(f"You used {skill_name} and caused {damage} damage")
                        user_character.cooldowns[skill_name] = user_character.skills[skill_name][
                            'cooldown']  # this is where we put the value of cooldown
                        return available_skills[skill_name]['damage']
            except ValueError:
                print("Invalid input. Try again")

    def start_Ai_against_AI(self, med_ai, ai):
        while True:  # both players are alive
            print(f"{med_ai.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = Medium_AI_Agent.use_skill(med_ai)  # player 1 uses skill
            if self.criticial(med_ai, ai, Attack):  # check if the attack will result in a critical hit
                ai.health -= Attack
            if ai.health <= 0:
                print(f"{ai.user_name} has been slain!")
                return 0

            print(f"{ai.user_name}'s Health:{ai.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"{ai.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = AI_Agent.use_skill(ai)  # ai uses skill
            if self.criticial(ai, med_ai, Attack):
                med_ai.health -= Attack

            if med_ai.health <= 0:
                print(f"{med_ai.user_name} has been slain!")
                return 0

            print(f"{med_ai.user_name}'s Health:{med_ai.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

            # Decrement cooldowns
            for skill in med_ai.cooldowns.keys():
                if med_ai.cooldowns[skill] > 0:
                    med_ai.cooldowns[skill] -= 1
            for skill in ai.cooldowns.keys():
                if ai.cooldowns[skill] > 0:
                    ai.cooldowns[skill] -= 1



game = Game()
# player_1 = game.choose_character()
MED_AI = AI_Agent.choose_character()
# player_2 = game.choose_character() # human player
# AI_player = AI_Agent.choose_character()
EASY_AI = Medium_AI_Agent.choose_character()
# game.start_against_AI(player_1, AI_player)
game.start_Ai_against_AI(MED_AI, EASY_AI)
