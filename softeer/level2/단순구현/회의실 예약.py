import sys

# Takinig Inputs
n, m = map(int, sys.stdin.readline().split())
rooms = [sys.stdin.readline().rstrip() for _ in range(n)]
conferences = [sys.stdin.readline().rstrip() for _ in range(m)]
rooms.sort()
rooms_dict = {rooms[i]: i for i in range(n)}

# Define Time Check List for Conferences
times = [[0] * 9 for _ in range(n)]
TIME_CONSTANT = 9

# Fill the Check List in
for conference in conferences:
    room, start, end = conference.split()
    start, end = int(start) - TIME_CONSTANT, int(end) - TIME_CONSTANT
    for i in range(start, end):
        times[rooms_dict[room]][i] = 1

# Getting Conference Times and Print out
for j, time in enumerate(times):
    start, end = 0, 0
    conference_time_list = []
    is_available = False
    conference_cnt = 0
    print(f"Room {rooms[j]}:")
    for i in range(len(time)):
        if time[i] == 0:
            is_available = True
            start, end = i, i+1
            conference_cnt += 1
            while (i+1) < len(time) and time[i+1] == 0:
                end += 1
                time[i+1] = 1 
                i += 1
            start, end = '{:02d}'.format(start+TIME_CONSTANT), '{:02d}'.format(end+TIME_CONSTANT)
            conference_time_list.append((start, end))
            
    if not is_available:
        print("Not available")
    else:
        print(f"{conference_cnt} available:")
        for start, end in conference_time_list:
            print(f"{start}-{end}")

    if j != len(times) - 1:
        print("-----")

    
