def swap_ele(items):
    if len(items) == 1:
        return items
    else:
        new_items = (items[-1],) + items[1:-1] + (items[0],)
        return new_items

items = tuple(map(int, input('Enter numbers:').split()))
print(swap_ele(items))