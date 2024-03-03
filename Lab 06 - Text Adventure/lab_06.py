class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # Bedroom
    room = Room('You are in the bedroom. There are doors to the North and East.', 5, 1, None, None)
    room_list.append(room)

    # Main hall
    room = Room('You are in the main hall. There are doors to the North, East, and West.', 6, 2, None, 0)
    room_list.append(room)

    # Dining hall
    room = Room('You are in the dining room. There are doors to the North, South, and West.', 4, None, 3, 1)
    room_list.append(room)

    # Kitchen
    room = Room('You are in the kitchen. There is a door to the North.', 2, None, None, None)
    room_list.append(room)

    # Study
    room = Room('You are in the study. There is a door to the South. ', None, None, 2, None)
    room_list.append(room)

    # Bathroom
    room = Room('You are in the bathroom. There are doors to the East and South. ', None, 1, 0, None)
    room_list.append(room)

    # Courtyard
    room = Room('You are in the courtyard. There is a door to the South.', None, None, 1, None)
    room_list.append(room)

    while not done:
        print(room_list[current_room].description)
        direction = input('Which way would you like to go? (n, s, e, w, or q to quit): \n').lower()

        if direction == 'n' or 'north' and room_list[current_room].north is not None:
            next_room = room_list[current_room].north
        elif direction == 's' or 'south' and room_list[current_room].south is not None:
            next_room = room_list[current_room].south
        elif direction == 'e' or 'east' and room_list[current_room].east is not None:
            next_room = room_list[current_room].east
        elif direction == 'w' or 'west' and room_list[current_room].west is not None:
            next_room = room_list[current_room].west
        else:
            print('Please pick a valid direction.\n')
            continue
        current_room = next_room


main()
