visits = 0

def trackVisits():
    global visits
    visits += 1
    return visits

print(trackVisits())
print(trackVisits())
print(trackVisits())
print(trackVisits())
print(trackVisits())



