visits = 0
def track_visits(page):
    global visits
    visits += 1
    print(f"User visited {page}. Total visits: {visits}")

track_visits("Home")
track_visits("About")
print(visits)