import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    for game_data in json_data:
        title = game_data["title"]
        year = game_data["year"]
        platform_name = game_data["platform"]["name"]
        platform_launch_year = game_data["platform"]["launch_year"]

    #Create Game and Platform objects
        platform = test_data.Platform(platform_name, platform_launch_year)
        game = test_data.Game(title, year, platform)

    return game_library


#Part 2
input_json_file = "data/test_data.json"

with open(input_json_file, "r") as json_file:
    json_data = json.load(json_file)

# Convert to GameLibrary data
game_library = make_game_library_from_json(json_data)

# Print the GameLibrary 
print(game_library) 