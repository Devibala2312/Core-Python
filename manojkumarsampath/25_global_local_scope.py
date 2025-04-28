# Global variable
visits = 0

# Function to track visits
def track_visit(page):
    global visits
    visits += 1
    message = f"User visited {page}. Total visits: {visits}"
    print(message)

# Example usage
track_visit("Home Page")
track_visit("About Page")
