total_hours = 108

hours = {
    '25/7' : 5, # Monday
    '26/7' : 5, # Tuesday
    '27/7' : 5, # Wednesday
    '28/7' : 5, # Thursday
    '29/7': 5, # Friday
    '30/7': 3, # Saturday
    '31/7': 1, # Sunday

    '1/8': 4, # Monday
    '2/8': 4.5, # Tuesday
    '3/8': 2.5, # Wednesday
    '4/8': 4.5, # Thurday
    '5/8': 5, # Friday
    '6/8': 0, # Saturday
    '7/8': 1.3, # Sunday
    '8/8': 5, # Monday
    '9/8': 5, # Tuesday
    '10/8': 5, # Wednesday
    '11/8': 5, # Thursday
    '12/8': 5, # Friday
    '13/8': 2, # Saturday
    '14/8': 2, # Sunday

    '15/8': 5, # Monday
    '16/8': 5, # Tuesday
    '17/8': 5, # Wednesday
    '18/8': 4.5, # Thursday
}

hours_so_far = sum(hours.values())
print(f"Hours: {hours_so_far}")
print(f"Hours to go: {total_hours-hours_so_far}")
print(f"{round((hours_so_far/total_hours)*100)}% complete")
bar = "-"*10
for i, char in enumerate(bar):
    if i < (hours_so_far/total_hours)*10:
        bar = bar[:i] + "=" + bar[i + 1:]

print(f"[ {bar} ]")
print(f"Pay: £{hours_so_far*5}")
