def likes(names):
    if names == None:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + "likes this"
    if len(names) == 2:
        return names[0] +" and "+ names[1] + "like this"
    if len(names) == 3:
        return names[0] + ", "+ names[1] + " and "+ names[2] + " likes this"
    if len(names) >= 4:
        return names[0] +", "+ names[1] + "and 2 others like this"  

print(
likes([]),
likes(['Peter']),
likes(['Jacob', 'Alex']),
likes(['Max', 'John', 'Mark']),
likes(['Alex', 'Jacob', 'Mark', 'Max']))