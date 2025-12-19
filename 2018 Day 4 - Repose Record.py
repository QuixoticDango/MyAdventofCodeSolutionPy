from datetime import datetime, timedelta

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 4 Advent of Code Input.txt"

with open(file, 'rt') as f:
    schedule = [line.strip().split('] ') for line in f.readlines()]

for i, s in enumerate(schedule):
    num= ''
    date_and_time = []
    for j, ch in enumerate(s[0][1:]):
        if ch.isnumeric():
            num += ch
        if not ch.isnumeric() or j == len(s[0][1:]) - 1:
            date_and_time.append(int(num))
            num = ''
    y, m, d, h, min = date_and_time
    schedule[i] = [datetime(y, m, d, h, min), s[1]]

schedule.sort(key=lambda s: s[0])
# stream = open(r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 4 Advent of Code Sorted.txt", 'wt')
# for s in schedule:
#     stream.write('['+ str(s[0]) + "] " + s[1] + '\n')
# stream.close()
guards = dict()
for i, s in enumerate(schedule):
    time, action = s
    if "Guard" in action:
        key = ''.join(ch for ch in action if ch == '#' or ch.isnumeric())
        if key not in guards.keys():
            guards[key] = []
            time_worked = time
    if 'falls' in action:
        time_slept = time
    if 'wakes' in action:
        time_slept = time - time_slept
        guards[key].append(time_slept)

max_time = timedelta(0)
for guard in guards.keys():
    sum = timedelta(0)
    for td in guards[guard]:
        sum += td
    if sum > max_time:
        laziest_guard = guard
        max_time = sum

guard_dict = dict()
for i, s in enumerate(schedule):
    time, action = s
    if '#' in action:
        key = ''.join(ch for ch in action if ch == '#' or ch.isnumeric())
        if key not in guard_dict.keys():
            guard_dict[key] = []
    guard_dict[key].append((time, action))

minutes = {i:0 for i in range(60)}
for date, action in guard_dict[laziest_guard]:
    if "falls" in action:
        start = date.minute
    if "wakes" in action:
        for min in range(start, date.minute):
            minutes[min] += 1

most_slept_on_minute = [minute for minute in minutes.keys() 
                        if minutes[minute] == max(minutes[minute] 
                                                  for minute in minutes.keys())][0]
print(most_slept_on_minute * int(laziest_guard[1:]))

guard_mins = dict()
for guard in guard_dict.keys():
    guard_mins[guard] = {i:0 for i in range(60)}
    for date, action in guard_dict[guard]:
        if "falls" in action:
            start = date.minute
        if "wakes" in action:
            for min in range(start, date.minute):
                guard_mins[guard][min] += 1

most_freq_sleep_guard_min = [(g, min) for g in guard_mins.keys() for min in guard_mins[g].keys()
                       if guard_mins[g][min] == max(guard_mins[g][min]
                                                    for g in guard_mins.keys()
                                                    for min in guard_mins[g].keys())][0]

print(int(most_freq_sleep_guard_min[0][1:]) * int(most_freq_sleep_guard_min[1]))