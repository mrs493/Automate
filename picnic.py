Guests = {'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham sandwiches': 3, 'apples': 2},
        'Carol': {'cups': 3, 'apple pies': 1}}

def totalBought(guests, item):
    numBrought = 0
    for guest in guests.values():
        numBrought += guest.get(item,0)
    return numBrought

print(totalBought(Guests, 'apples'))