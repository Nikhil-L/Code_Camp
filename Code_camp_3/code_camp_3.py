class Customer:

    def __init__(self):
        self.name = None
        self.list_of_items = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_item(self, item):
        self.list_of_items.append(item)
    
    def get_items_list(self):
        return self.list_of_items

    def calculate_bill(self):
        total_cost = 0
        for i in self.list_of_items:
            total_cost = total_cost + i.get_price()
        return total_cost


class Item:

    def __init__(self):
        self.name = None
        self.price = None

    def set_item(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price



def main():
    customer = Customer()
    customer.set_name("Ravi")
    item1, item2 = Item(), Item()
    item1.set_item("Rice", 100)
    item2.set_item("Oil", 200)
    customer.add_item(item1)
    customer.add_item(item2)
    print("Customer bill is : ", customer.calculate_bill())


if __name__ == '__main__':
    main()
