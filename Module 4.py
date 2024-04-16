# This is the class called ItemToPurchase
class ItemToPurchase:
    # the default constructor is initialized and attributes for products
    def __init__(self):
        # initialize attributes
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    # the method print_item_cost()
    # print the cost
    def print_item_cost(self):
        # print output in format
        print(self.item_name, self.item_quantity, '@ $', end='')
        print(self.item_price, '= $', end='')

        # calculations performed here
        cost = self.item_price * self.item_quantity
        print(cost)


# Condition statement
if __name__ == "__main__":

    # create two object variables for items
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    # user input
    print('Item 1')
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))

    # for item 2
    print('\nItem 2')
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    # print costs
    print('TOTAL COST')
    # display the item cost
    item1.print_item_cost()
    item2.print_item_cost()

    # display total cost
    print('\nTotal: $', end='')
    # for item1 and item2
    total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print(total_cost)