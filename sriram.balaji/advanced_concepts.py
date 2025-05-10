# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 09:22:55 2025

@author: sriram.balaji
"""

###Scopes Global vs local pagevisit

visits = 0

def track_visit(page):
    global visits  
    visits += 1
    message = f"User visited {page}. Total visits: {visits}"  # Local variable
    print(message)


track_visit("Homepage")
track_visit("Homepage")
track_visit("About Us")
track_visit("Contact")
print(visits)
