import sys

n, m = map(int, sys.stdin.readline().split())
rooms = [sys.stdin.readline().rstrip() for _ in range(n)]
conferences = [sys.stdin.readline().rstrip() for _ in range(m)]
rooms.sort()
rooms_dict = {rooms[i]: i for i in range(n)}
print(rooms_dict)
print(n, m)
print(rooms)
print(conferences)

times = [[0] * 9 for _ in range(n)]
print(times)

for conference in conferences:
    room, start, end = conference.split()
    start, end = int(start), int(end)
    for i in range(start - 9, end - 9):
        times[rooms_dict[room]][i] = 1
print(times)
