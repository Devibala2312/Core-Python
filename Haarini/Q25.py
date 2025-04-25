#  print("\nTask 25:")

visits = 0
def track_visit(page="page"):
  global visits
  visits += 1
  message = f"User visited {page}. Total visits: {visits}"
  print(message)

track_visit("Home")     
track_visit("About")  
track_visit()  