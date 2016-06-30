k = int(input())
room_no = input().split()
uniq_rooms = set()
duplicate_rooms = set()

for room in room_no:
    if room in uniq_rooms:
        uniq_rooms.remove(room)
        duplicate_rooms.add(room)
    elif room not in duplicate_rooms:
        uniq_rooms.add(room)
        
print(next(iter(uniq_rooms)))