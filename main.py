import json
import os
import glob

global_character_path = "./characters"
global_game_path = "./game"

if not os.path.exists(global_character_path):
    os.makedirs(global_character_path)

if not os.path.exists(global_game_path):
    os.makedirs(global_game_path)

character_list = []
realm_list = []

# print(glob.glob(global_character_path+"/*"))
for file in glob.glob(global_character_path + "/*"):
    character_list.append(file)


def print_with_index(list_to_print: list):
    for char in range(len(list_to_print)):
        print(char, list_to_print[char])


print_with_index(character_list)


class singular_json_print:
    def __init__(self, json_print):
        self.json_print = json_print

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class realm:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class character_template:
    def __init__(self, character_name, age, race, height, proficiency):
        self.character_name = character_name
        self.age = age
        self.race = race
        self.height = height
        self.proficiency = proficiency

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def read_from_json(json_path: str):
    with open(json_path.replace(" ", "_"), "r") as json_file:
        data = json.load(json_file)
    json_file.close()
    return data


def add_to_prev_json(json_path: str, input_to_file: str):
    with open(json_path.replace(" ", "_"), "w+") as json_file:
        input_to_file = singular_json_print(input_to_file).toJSON()
        w = json.dumps(input_to_file)
        json_file.write(w)


# temp = input("Test: ")
# add_to_prev_json("test.json", temp)

# print(read_from_json("test.json"))

def create_realm(realm_name: str, difficulty: int):
    if difficulty > 10 or difficulty < 0:
        print("Please enter a valid difficulty level.")
    else:
        if not os.path.exists(global_game_path + "/GAME.json"):
            r = realm(realm_name, difficulty).toJSON()
            json_settings = json.dumps(r)

            wn_fixed = global_game_path + "/" + realm_name + ".json"
            wn_fixed = str(wn_fixed).replace(" ", "_")
            with open(wn_fixed, "w") as jsonfile:
                jsonfile.write(json_settings)
            jsonfile.close()


def create_character(character_name: str, age: int, race: str, height: int, proficiency: str):
    if age <= 0:
        print("Please enter a valid age.")
    else:
        if not os.path.exists(global_character_path + "/GAME.json"):
            r = character_template(character_name, age, race, height, proficiency).toJSON()
            json_settings = json.dumps(r)

            wn_fixed = global_character_path + "/" + character_name + ".json"
            wn_fixed = str(wn_fixed).replace(" ", "_")
            with open(wn_fixed, "w") as jsonfile:
                jsonfile.write(json_settings)
            # character_list.append(wn_fixed)

            jsonfile.close()


def print_character_information(char_name: str):
    read_from_json(global_character_path + "/" + char_name + ".json")


def list_dir(dir_to_list: str, num: bool):
    files = os.listdir("./" + dir_to_list)
    if num:
        i = 0
        print("---------------------------------")
        for f in files:
            print(f"[{i}]" + f.replace(".json", "") + ", ", end="")
            i += 1
        print("\n---------------------------------")
        print("\n")
    else:
        print("---------------------------------")
        for f in files:
            print(f.replace(".json", "") + ", ", end="")
        print("\n---------------------------------")
        print("\n")


def delete_character(character_name: str):
    # character_name = character_name.lower()
    if os.path.exists(global_character_path + "/" + character_name + ".json"):
        try:
            os.remove(global_character_path + "/" + character_name + ".json")
            print("File: '" + character_name + "' deleted.")
        except:
            print("Cannot delete character file.")
    else:
        print("Character file does not exist.")


def main():
    while True:
        # answ = input("What would you like to do? [ Create Realm[CR], List All Realms[LR], List Realm Information[LR + "
        #             "´Realm Name´] , Create Character[CC], List All Characters[LC], List Char Information[LC + "
        #             "´Character Name´] "
        #             ", Delete Character[DC], Exit[E,Q] ]: ")

        answ = input("\n ------------------- "
                     "\n  - Realms -"
                     "\n[cr] - Create a new realm"
                     "\n[lr] - List all realms"
                     "\n[lr + ´realm_name´] - List Specific Realm Information"
                     "\n[dr] - Delete Realm"
                     "\n ------------------- "
                     "\n  - Characters -"
                     "\n[cc] - Create a new character"
                     "\n[lc] - List all characters"
                     "\n[lc + ´character_name´] - List Specific Character Information"
                     "\n[dc] - Delete character"
                     "\n ------------------- "
                     "\n  - Misc -"
                     "\n[h] - This Help Message"
                     "\n: ")

        if answ.lower() == "h" or answ.lower() == "help":
            print("\n ------------------- "
                  "\n  - Realms -"
                  "\n[cr] - Create a new realm"
                  "\n[lr] - List all realms"
                  "\n[lr + ´realm_name´] - List Specific Realm Information"
                  "\n[dr] - Delete Realm"
                  "\n ------------------- "
                  "\n  - Characters -"
                  "\n[cc] - Create a new character"
                  "\n[lc] - List all characters"
                  "\n[lc + ´character_name´] - List Specific Character Information"
                  "\n[dc] - Delete character"
                  "\n ------------------- "
                  "\n  - Misc -"
                  "\n[h] - This Help Message"
                  "\n: ")

        # Create New Realm
        elif answ.lower() == "cr":
            realm_name = input("Name of new realm: ")
            realm_difficulty = input("Difficulty of " + '"' + realm_name + '"' + "[1-10].: ")

            create_realm(realm_name, int(realm_difficulty))
            print(read_from_json(global_game_path + "/" + realm_name + ".json"))

        # Create New Character
        elif answ.lower() == "cc":
            character_name = input("Name of new character: ")
            char_age = input("Age of character(int): ")
            char_race = input("Race of character(elf, dragonborn, human etc.): ")
            char_height = input("Height of character(cm): ")
            char_proficiency = input("Character proficiency: ")
            create_character(character_name, int(char_age), char_race, int(char_height), char_proficiency)

        # List All Realms
        elif answ.lower() == "lr":
            list_dir("game", True)

        # List All Characters
        elif answ.lower() == "lc":
            list_dir("characters", True)

        # List Specific Character Information
        elif answ.lower().__contains__("lc") and answ.lower().__contains__(" "):
            answ = answ.replace("lc", "")
            answ = answ.replace(" ", "")
            print(read_from_json(global_character_path + "/" + answ + ".json"))

        # List Specific Realm Information
        elif answ.lower().__contains__("lr") and answ.lower().__contains__(" "):
            answ = answ.replace("lr", "")
            answ = answ.replace(" ", "")
            print(read_from_json(global_game_path + "/" + answ + ".json"))

        # Delete Character
        elif answ.lower() == "dc":
            list_dir(dir_to_list="characters", num=False)
            char_to_delete = input("What character would you like to delete?(Type the full name ´Upper Lowercase "
                                   "Sensitive´) ")
            delete_character(char_to_delete)

        # Terminate Program
        elif answ.lower() == "e" or answ.lower() == "q":
            exit(0)


if __name__ == '__main__':
    main()
