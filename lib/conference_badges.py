def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names : list):
    i = 0
    return [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]

def printer(names):
    [print(item) for item in batch_badge_creator(names)]
    [print(item) for item in assign_rooms(names)]
