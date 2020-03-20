from room import Room
from player import Player
from world import World
from queue import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = ['n', 'n']

backwards_directions = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e"
}

def traverse():
    visited = []
    path = []
    last_direction = []

    while True:
        new_room = False
        path.append(player.current_room.id)

        if len(visited) == len(world.rooms):
            break

        for direction in player.current_room.get_exits():
            room = player.current_room.get_room_in_direction(direction)

            if room.id not in visited:
                last_direction.append(direction)
                visited.append(room.id)
                player.travel(direction)
                new_room = True
                break

        if new_room == False:
            if last_direction == []:
                break

            player.travel(backwards_directions[last_direction[-1]])
            last_direction.pop()

    
    moves = []

    cur_room = world.starting_room

    for idx in range(1, len(path)):
        room_id = path[idx]

        for direction in cur_room.get_exits():
            room_in_direction = cur_room.get_room_in_direction(direction)

            if room_in_direction.id == room_id:
                moves.append(direction)
                cur_room = room_in_direction
                break

    return moves



traversal_path = traverse()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
