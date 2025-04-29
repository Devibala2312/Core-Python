visits = 0

def track_visit(page):
    global visits
    visits += 1
    print(f"User visited {page}. Total visits:", visits)

track_visit("Home")
track_visit("About")
print(visits)