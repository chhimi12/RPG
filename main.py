import random

import character
from character import Knight, Mage
import easy_ai
from easy_ai import AI_Agent
from medium_ai import Medium_AI_Agent


def apply_buff(user_character, type, duration, amount, counter):

    if type == "Health Buff":
        # Issue with health buff: its as a proportion of current health. Instead of max health.
        # can have a new max health attribute in character, or pass down initial health into apply
        previous_health = user_character.health
        print("Current Health: " + str(previous_health))
        Increase = user_character.max_health * amount # 0.5 * max health
        user_character.health += Increase
        print(f"Health increased by {round(Increase, 2)} points \n")
        print(f"your health is now {user_character.health} ")

    elif type == "Attack Buff":
        user_character.attack *= amount
        print(f"Attack increased by {round((amount - 1) * 100, 2)}%")

    elif type == "Defense Buff":
        user_character.defense *= amount
        print(f"Defense increased by {round((amount - 1) * 100, 2)}%")

    elif type == "Critical Buff":
        user_character.critical_hit_rate *= amount
        print(f"Critical hit rate increased by {round((amount - 1) * 100, 2)}%")

    elif type == "Dodge Buff":
        user_character.dodge_rate *= amount
        print(f"Dodge rate increased by {round((amount - 1) * 100, 2)}%")
    user_character.active_buff = True


def remove_buff(user_character, type, duration, amount, counter):
    print("The effects of the buff are over. \n")
    if type == "Health Buff":
        pass  # do nothing permanet buff

    elif type == "Attack Buff":
        user_character.attack /= amount
        print(f"Attack has been reverted to {user_character.attack}%")

    elif type == "Defense Buff":
        user_character.defense /= amount
        print(f"Defense has been reverted to {user_character.defense}%")

    elif type == "Critical Buff":
        user_character.critical_hit_rate /= amount
        print(f"Critical hit rate has been reverted to  {user_character.critical_hit_rate}")

    elif type == "Dodge Buff":
        user_character.dodge_rate /= amount
        print(f"Dodge rate has been reverted to {user_character.dodge_rate}%")


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

            if random.random() > ai.dodge_rate: # if not dodged
                Attack = self.criticial(player_1, Attack)  # if true increase damage
                damage_absorption = 0.05 * ai.defense
                if damage_absorption < Attack:  # if atttack is greater, so we don't have a negtaive attack value
                    Attack = Attack - round(damage_absorption, 2)
                else:
                    Attack = 0  # complete absorpotion
                print(f"you caused {Attack} damage.")
                print(f"Health({round(ai.health,2)}) - Damage({round(Attack,2)})")
                ai.health -= Attack  # reduce health

            elif Attack != 0 : # if its not a buff
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
                print(f"Health({round(ai.health,2)}) - Damage({round(Attack,2)})")
                player_1.health -= Attack  # reduce health

            elif Attack != 0 :
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
                    Attack = Attack - round(damage_absorption, 2)
                else:
                    Attack = 0

                print(f"You caused {Attack} damage.")
                print(f"Health({round(player_2.health,2)}) - Damage({round(Attack)}")
                player_2.health -= Attack

            elif Attack != 0 : # if its not a buff skill
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
                print(f"Health({round(player_1.health, 2)}) - Damage({round(Attack)}")
                player_1.health -= Attack

            elif Attack != 0:
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
                choice = input("Type the name of the skill to use the skill or type 'hit' to use a basic attack"
                               "\n Type 'skill_info' to view your skills information: ")

                if choice == "hit":
                    print(f"You used a basic attack. \n")
                    return user_character.attack
                if choice == "skill_info":
                    for category, skills_dict in user_character.skills.items():
                        print(f"{category}:")
                        for skill, details in skills_dict.items():
                            print(f"\t{skill}:")
                            for attribute, value in details.items():
                                print(f"\t\t{attribute}: {value}")
                    choice = input("Type the name of the skill to use the skill or type 'hit' to use a basic attack"
                                   "\n Type 'skill_info' to view your skills information: ")
                # if skill exists
                if any(choice in skills_category for skills_category in user_character.skills.values()):
                    # check if skill is in cool down
                    if user_character.cooldowns[choice] > 0:  # at first its initialized to 0
                        print(f"{choice} is still on cooldown for {user_character.cooldowns[choice]} turns.")

                    else:
                        print(f"You used {choice}.")

                        # check if there is an active buff
                        if user_character.active_buff: # if there is an active buff, icnrement the counter for them each turn
                                if user_character.skills['Buff_skills'][user_character.buff_in_effect]["Counter"] > user_character.skills['Buff_skills'][user_character.buff_in_effect]["Duration"]:  # check if buff effect is over

                                    user_character.active_buff = False
                                    remove_buff(user_character, user_character.skills['Buff_skills'][user_character.buff_in_effect]["Buff Type"],user_character.skills['Buff_skills'][user_character.buff_in_effect]["Duration"],user_character.skills['Buff_skills'][user_character.buff_in_effect]["Amount"],
                                                user_character.skills['Buff_skills'][user_character.buff_in_effect]["Counter"])  # reset all stats to normal
                                    user_character.skills['Buff_skills'][user_character.buff_in_effect][
                                        "Counter"] = 0  # set counter to 0 if buff effect is over
                                else:  # if not over, incremet the counter
                                    user_character.skills['Buff_skills'][user_character.buff_in_effect]["Counter"] += 1
                                    # if the user uses a buff skill

                       # if chosen move is a buff skill
                        if choice in user_character.skills['Buff_skills']:
                            type = user_character.skills['Buff_skills'][choice]["Buff Type"]
                            duration = user_character.skills['Buff_skills'][choice]["Duration"]
                            amount = user_character.skills['Buff_skills'][choice]["Amount"]
                            counter = user_character.skills['Buff_skills'][choice]["Counter"]

                            if not user_character.active_buff:
                                # apply the buff
                                apply_buff(user_character, type, duration, amount, counter)
                                user_character.cooldowns[choice] = user_character.skills['Buff_skills'][choice][
                                    "cooldown"]
                                user_character.buff_in_effect = choice
                                return user_character.skills['Buff_skills'][choice]["damage"]
                            else:
                                print("You already have an active buff.")
                                continue

                        else:  # if its an attack skill return the damage
                            # set cool down counter
                            user_character.cooldowns[choice] = user_character.skills['attack_skills'][choice][
                                "cooldown"]
                            return user_character.skills['attack_skills'][choice]["damage"]
                else:
                    print(f"A skill called {choice} doesn't exist, is there a typo?")
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
                print(f"Health({round(ai.health,2)}) - Damage({round(Attack,2)})")
                ai.health -= Attack

            elif Attack != 0 :
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
                print(f"Health({round(med_ai.health, 2)}) - Damage({round(Attack, 2)})")
                med_ai.health -= Attack

            elif Attack != 0:
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
# MED_AI = AI_Agent.choose_character()
EASY_AI = AI_Agent.choose_character()
game.start_Ai_against_AI(MED_AI,EASY_AI)
# player_2 = game.choose_character()  # human player
# player_1 = game.choose_character()  # human player
# AI_player = AI_Agent.choose_character()
# game.start(player_1, player_2)
