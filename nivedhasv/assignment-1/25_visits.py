# 25. Scopes - local & global:
# You have a global variable visits initialized to 0.
# Write a function track_visit(page) that:
# Increments the global visits by 1 each time it’s called.
# Creates a local variable called message like: "User visited {page}. Total visits: {visits}"
# Prints the message.

visits = 0

def track_visit(page):
    global visits
    visits += 1
    print(f"User visited {page}. Total visits: {visits}")

track_visit("home")
track_visit("about")
print(visits)

