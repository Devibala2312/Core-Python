visits = 0
def trackVisit(page):
    global visits
    visits += 1
    message = f"User visited {page}. Total counts {visits}"
    print(message)
trackVisit('login')
trackVisit('about')