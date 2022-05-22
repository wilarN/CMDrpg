import json
import os
import sys

global_character_path = "./characters"
global_game_path = "./game"

if not os.path.exists(global_character_path):
    os.makedirs(global_character_path)

if not os.path.exists(global_game_path):
    os.makedirs(global_game_path)


class realm:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def read_from_json(json_path: str):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
    json_file.close()
    return data


def create_realm(realm_name: str, difficulty: int):
    if difficulty > 10 or difficulty < 0:
        print("Please enter a valid difficulty level.")
    else:
        if not os.path.exists(global_game_path + "/GAME.json"):
            r = realm(realm_name, difficulty).toJSON()
            json_settings = json.dumps(r)

            with open(global_game_path + "/" + realm_name + ".json", "w") as jsonfile:
                jsonfile.write(json_settings)
            jsonfile.close()


def create_character():
    pass


def list_characters():
    pass


def delete_character():
    pass


def main():
    while True:
        answ = input("What would you like to do? [ Create Realm[CR], List All Realms[L] ]")

        # Create New Realm
        if answ.lower() == "cr":
            realm_name = input("Name of new realm: ")
            realm_difficulty = input("Difficulty of " + '"' + realm_name + '"' + "[1-10].: ")

            create_realm(realm_name, int(realm_difficulty))
            print(read_from_json(global_game_path + "/" + realm_name + ".json"))

        # List All Realms
        if answ.lower() == "l":
            files = os.listdir("./game")
            i = 0
            print("---------------------------------")
            for f in files:
                print(f"[{i}]" + f.replace(".json", "") + ", ", end="")
                i += 1
            print("\n---------------------------------")
            print("\n")


if __name__ == '__main__':
    main()
