def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for item, amount in inventory.items():
        print(amount, item)
        total += amount
    print('Total number of items:', total, end='\n\n')

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inventory)
addToInventory(inventory, dragonLoot)
displayInventory(inventory)