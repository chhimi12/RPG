import random

import character
from character import Knight, Mage
import easy_ai
from easy_ai import AI_Agent
from medium_ai import Medium_AI_Agent


class Game:

    def criticial(self, attacker, attack):  # modifies attack if critical hit rate is achieved
        if random.random() < attacker.critical_hit_rate:
            attack = 1.5 * attack
            print(f"{attacker.user_name} landed a critical hit!")
        return attack  # Attack hit

    def start_against_AI(self, player_1, ai):
        while True:  # both players are alive
            print(f"{player_1.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_1)  # player 1 uses skill
            # if atk is NOT dodged
            if random.random() > ai.dodge_rate:
                Attack = self.criticial(player_1, Attack)  # if true increase damage
                damage_absorption = 0.05 * ai.defense
                if damage_absorption < Attack:  # if atttack is greater, so we don't have a negtaive attack value
                    Attack = Attack - round(damage_absorption, 2)
                else:
                    Attack = 0  # complete absorpotion
                print(f"you caused {Attack} damage.")
                print(f"Health({ai.health}) - Damage({Attack})")
                ai.health -= Attack  # reduce health

            else:
                print(f"{ai.user_name} dodged the attack!")

            if ai.health <= 0:
                print(f"{ai.user_name} has been slain!")
                return 0

            print(f"{ai.user_name}'s Health:{ai.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print(f"{ai.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = Medium_AI_Agent.use_skill(ai)  # medium ai uses skill
            # if atk is NOT dodged
            if random.random() > player_1.dodge_rate:
                Attack = self.criticial(ai, Attack)  # if true increase damage
                damage_absorption = 0.05 * player_1.defense
                if damage_absorption < Attack:  # if atttack is greater, so we don't have a negtaive attack value
                    Attack = Attack - round(damage_absorption, 2)
                else:
                    Attack = 0  # complete absorpotion
                print(f"{ai.user_name} caused {Attack} damage.")
                print(f"Health({ai.health}) - Damage({Attack})")
                player_1.health -= Attack  # reduce health

            else:
                print(f"{player_1.user_name} dodged the attack!")

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
            # Dodge Check
            if random.random() > player_2.dodge_rate:
                # Attack successful - Apply critical hit and damage absorption
                Attack = self.criticial(player_1, Attack)  # Check for critical hit
                damage_absorption = 0.05 * player_2.defense

                if damage_absorption < Attack:
                    Attack = Attack - round(damage_absorption,2)
                else:
                    Attack = 0
                print(f"You caused {Attack} damage.")
                print(f"Health({player_2.health}) - Damage({Attack})")
                player_2.health -= Attack

            else:
                print(f"{player_2.user_name} dodged the attack!")

            if player_2.health <= 0:
                print(f"{player_2.user_name} has been slain!")
                return 0

            print(f"{player_2.user_name}'s Health:{player_2.health}")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

            print(f"{player_2.user_name}'s turn")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            Attack = self.use_skill(player_2)  # player 2 attack player 1
            # Dodge Check
            if random.random() > player_1.dodge_rate:
                # Attack successful - Apply critical hit and damage absorption
                Attack = self.criticial(player_2, Attack)  # Check for critical hit
                damage_absorption = 0.05 * player_1.defense
                if damage_absorption < Attack:
                    Attack = Attack - round(damage_absorption, 2)
                else:
                    Attack = 0
                print(f"You caused {Attack} damage.")
                print(f"Health({player_1.health}) - Damage({Attack})")
                player_1.health -= Attack

            else:
                print(f"{player_1.user_name} dodged the attack!")

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
                    print(f"You used a basic attack ")
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
                    if user_character.cooldowns[skill_name] > 0:  # at first its initialized to 0
                        print(f"{skill_name} is still on cooldown for {user_character.cooldowns[skill_name]} turns.")
                    else:
                        damage = available_skills[skill_name]['damage']
                        print(f"You used {skill_name}.")
                        user_character.cooldowns[skill_name] = user_character.skills[skill_name][
                            'cooldown']  # this is where we put the value of cooldown
                        return damage
            except ValueError:
                print("Invalid input. Try again")

    def start_Ai_against_AI(self, med_ai, ai):
            while True:  # both players are alive
                print(f"{med_ai.user_name}'s turn")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                Attack = Medium_AI_Agent.use_skill(med_ai)

                # Dodge Check for AI
                if random.random() > ai.dodge_rate:
                    # Attack successful - Apply critical hit and damage absorption
                    Attack = self.criticial(med_ai, Attack)  # Check for critical hit
                    damage_absorption = 0.05 * ai.defense
                    if damage_absorption < Attack:
                        Attack = Attack - round(damage_absorption, 2)
                    else:
                        Attack = 0
                    print(f"{med_ai.user_name} caused {Attack} damage.")
                    print(f"Health({ai.health}) - Damage({Attack})")
                    ai.health -= Attack

                else:
                    print(f"{ai.user_name} dodged the attack!")

                if ai.health <= 0:
                    print(f"{ai.user_name} has been slain!")
                    return 0

                print(f"{ai.user_name}'s Health:{ai.health}")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

                print(f"{ai.user_name}'s turn")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                Attack = AI_Agent.use_skill(ai)

                # Dodge Check for Med AI
                if random.random() > med_ai.dodge_rate:
                    # Attack successful - Apply critical hit and damage absorption
                    Attack = self.criticial(ai, Attack)  # Check for critical hit
                    damage_absorption = 0.05 * med_ai.defense
                    if damage_absorption < Attack:
                        Attack = Attack - round(damage_absorption, 2)
                    else:
                        Attack = 0
                    print(f"{ai.user_name} caused {Attack} damage.")
                    print(f"Health({med_ai.health}) - Damage({Attack})")
                    med_ai.health -= Attack

                else:
                    print(f"{med_ai.user_name} dodged the attack!")

                if med_ai.health <= 0:
                    print(f"{med_ai.user_name} has been slain!")
                    return 0

                print(f"{med_ai.user_name}'s Health:{med_ai.health}")
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

                # Decrement cooldowns for med_ai
                for skill in med_ai.cooldowns.keys():
                    if med_ai.cooldowns[skill] > 0:
                        med_ai.cooldowns[skill] -= 1
                for skill in ai.cooldowns.keys():
                    if ai.cooldowns[skill] > 0:
                        ai.cooldowns[skill] -= 1


game = Game()
MED_AI = Medium_AI_Agent.choose_character()
# EASY_AI = AI_Agent.choose_character()
# game.start_Ai_against_AI(MED_AI,EASY_AI)
player_1 = game.choose_character() # human player
AI_player = AI_Agent.choose_character()
game.start_against_AI(player_1, MED_AI)

