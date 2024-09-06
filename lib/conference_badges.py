def badge_maker(name):
    badge_message = f"Hello, my name is {name}."
    return badge_message

def batch_badge_creator(names):
    name_badges = [badge_maker(name) for name in names]
    return name_badges
     
def assign_rooms(names):
    room_assignments = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for room in assign_rooms(names):
        print(room)
       
       
    