value = {}
def track_visit(page):
    global value
    value[page] = value.get(page,0)+1
    return f"User visited {page}. Total visits: {value[page]}"
print(track_visit('Home'))
print(track_visit('About'))
print(track_visit('Home'))
print(track_visit('Home'))
print(track_visit('Welcome'))
print(track_visit('About'))